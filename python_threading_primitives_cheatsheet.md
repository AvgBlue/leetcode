# Python Multithreading Primitives Cheat Sheet

Focused on `threading` synchronization primitives.

```python
import threading
```

---

## 1. `Thread`

Runs a function in another thread.

```python
def work(x):
    print(x)

t = threading.Thread(target=work, args=(5,))

t.start()   # Start the thread
t.join()    # Wait until it finishes
```

### Mental model

- `start()` → let this thread begin running.
- `join()` → the current thread waits until that thread finishes.
- Starting threads in an order does **not** guarantee execution order.

---

## 2. `Lock` — Mutex

Use when **only one thread at a time** may access some shared resource.

```python
lock = threading.Lock()

with lock:
    # critical section
    do_work()
```

Equivalent to:

```python
lock.acquire()

try:
    do_work()
finally:
    lock.release()
```

### Important methods

```python
lock.acquire()
lock.release()
lock.locked()
```

Non-blocking attempt:

```python
if lock.acquire(blocking=False):
    try:
        do_work()
    finally:
        lock.release()
```

### Mental model

> One key. Only the thread holding the key may enter.

### Common use

```python
counter = 0
lock = threading.Lock()

def increment():
    global counter

    with lock:
        counter += 1
```

### Danger: deadlock

Bad:

```text
Thread A owns lock1 → waits for lock2
Thread B owns lock2 → waits for lock1
```

A common rule:

> Always acquire multiple locks in the same order.

---

## 3. `RLock` — Reentrant Lock

Like `Lock`, but the **same thread can acquire it multiple times**.

```python
lock = threading.RLock()

with lock:
    with lock:
        do_work()
```

Every acquisition must eventually have a corresponding release.

### Mental model

> A mutex that allows recursive/nested locking by its owner.

### Use when

A locked function may call another function that tries to acquire the same lock.

---

## 4. `Semaphore`

Allows up to **N threads** into a protected area at once.

```python
sem = threading.Semaphore(3)

with sem:
    do_work()
```

Or manually:

```python
sem.acquire()
do_work()
sem.release()
```

### Mental model

> A bucket containing N tickets.

Each `acquire()` takes a ticket.  
Each `release()` returns one.

If there are no tickets, the thread waits.

### Useful special case

```python
sem = threading.Semaphore(0)
```

No thread can initially pass `acquire()`.

Another thread can unlock progress with:

```python
sem.release()
```

This is useful for ordering threads.

```python
first_done = threading.Semaphore(0)

def first():
    print("first")
    first_done.release()

def second():
    first_done.acquire()
    print("second")
```

---

## 5. `BoundedSemaphore`

Like `Semaphore`, but detects accidental over-release.

```python
sem = threading.BoundedSemaphore(3)
```

If you call `release()` too many times, Python raises an error.

Use it when the semaphore represents a fixed-size resource pool.

---

## 6. `Event`

Represents a shared **true/false signal**.

```python
event = threading.Event()
```

Initially:

```text
false / unset
```

Wait:

```python
event.wait()
```

Signal:

```python
event.set()
```

Reset:

```python
event.clear()
```

Check without waiting:

```python
event.is_set()
```

### Mental model

> "Has something happened yet?"

Example:

```python
ready = threading.Event()

def producer():
    prepare_data()
    ready.set()

def consumer():
    ready.wait()
    use_data()
```

### Important behavior

Once an Event is set:

```python
event.set()
```

**all current and future `wait()` calls pass** until:

```python
event.clear()
```

This is different from a semaphore.

---

## 7. `Condition`

Use when threads need to wait until some **shared-state condition becomes true**.

```python
condition = threading.Condition()
state = 0
```

Waiting:

```python
with condition:
    condition.wait_for(lambda: state == 1)
```

Changing state:

```python
with condition:
    state = 1
    condition.notify_all()
```

### Main methods

```python
condition.wait()
condition.wait_for(predicate)
condition.notify()       # wake one waiter
condition.notify_all()   # wake all waiters
```

### Mental model

> "Wake me when shared state may have changed."

Typical cases:

- queue becomes non-empty
- buffer has free space
- program reaches a particular state
- producer / consumer coordination

Prefer:

```python
condition.wait_for(lambda: ready)
```

over manually doing:

```python
while not ready:
    condition.wait()
```

They express the same idea.

---

## 8. `Barrier`

Makes a fixed number of threads wait until **everyone reaches the same point**.

```python
barrier = threading.Barrier(3)
```

Each thread:

```python
do_phase_1()
barrier.wait()
do_phase_2()
```

Nobody passes until all 3 threads call `barrier.wait()`.

### Mental model

```text
Thread A ─────┐
Thread B ─────┼── all arrived → continue
Thread C ─────┘
```

### Useful for

Algorithms with phases:

```text
phase 1
↓
everyone synchronizes
↓
phase 2
```

---

# Quick Comparison

| Primitive | Main question |
|---|---|
| `Lock` | May only one thread enter? |
| `RLock` | May one thread lock recursively? |
| `Semaphore(n)` | May at most N threads enter? |
| `BoundedSemaphore(n)` | Same, but detect excess releases |
| `Event` | Has something happened yet? |
| `Condition` | Is some shared-state condition true? |
| `Barrier(n)` | Have all N threads arrived? |

---

# `Event` vs `Semaphore`

These can look similar but behave differently.

## Event

```python
event.set()
```

Once set:

```text
wait()
wait()
wait()
```

all pass.

It stays set until:

```python
event.clear()
```

## Semaphore

```python
sem.release()
```

adds **one permit**.

One:

```python
sem.acquire()
```

consumes that permit.

So:

```text
1 release → 1 acquire can pass
3 releases → 3 acquires can pass
```

### Rule of thumb

Use `Event` for:

> "This state/event has happened."

Use `Semaphore` for:

> "A certain number of permissions/resources are available."

---

# `Lock` vs `Event`

## Lock

```text
"Only one thread may use this resource."
```

Example:

```python
with lock:
    shared_data += 1
```

## Event

```text
"Wait until another thread signals that something happened."
```

Example:

```python
ready.wait()
```

---

# Ordering Threads

Suppose you need:

```text
first → second → third
```

## With Events

```python
first_done = threading.Event()
second_done = threading.Event()
```

Concept:

```text
first
  ↓ set first_done
second waits first_done
  ↓ set second_done
third waits second_done
```

## With Semaphores

```python
first_done = threading.Semaphore(0)
second_done = threading.Semaphore(0)
```

Concept:

```text
first
  ↓ release permit
second acquire permit
  ↓ release permit
third acquire permit
```

---

# Alternating Threads

For:

```text
foo bar foo bar foo bar
```

Think about **passing control back and forth**.

For example, two synchronization objects:

```text
foo_allowed
bar_allowed
```

Initially:

```text
foo_allowed = available
bar_allowed = blocked
```

After `foo` runs:

```text
block foo
allow bar
```

After `bar` runs:

```text
block bar
allow foo
```

This can be modeled naturally with semaphores.

---

# `with` and Waiting

When you write:

```python
with lock:
    do_work()
```

Python effectively does:

```text
try to acquire lock
↓
if unavailable → wait here
↓
lock acquired
↓
run block
↓
release lock
```

For a semaphore:

```python
with sem:
    do_work()
```

means:

```text
sem.acquire()
do_work()
sem.release()
```

---

# Useful Patterns

## Protect shared state

```python
lock = threading.Lock()

with lock:
    shared_state.update(...)
```

## Wait for initialization

```python
ready = threading.Event()
ready.wait()
```

## Limit concurrency

```python
limit = threading.Semaphore(5)

with limit:
    make_request()
```

## Wait for a state

```python
condition = threading.Condition()

with condition:
    condition.wait_for(lambda: queue_has_data)
```

## Synchronize phases

```python
barrier = threading.Barrier(worker_count)
barrier.wait()
```

---

# Common Mistakes

## 1. Assuming `start()` order is execution order

Wrong assumption:

```python
t1.start()
t2.start()
```

does **not** guarantee that `t1` executes first.

## 2. Forgetting to release a lock

Prefer:

```python
with lock:
    ...
```

instead of manual acquire/release whenever possible.

## 3. Acquiring multiple locks in inconsistent order

Keep one global order:

```text
lock1 → lock2 → lock3
```

## 4. Confusing state with permit count

`Event` stores a state.  
`Semaphore` stores a count.

## 5. Using synchronization you don't need

Choose based on the problem:

```text
exclusive resource    → Lock
N resource slots      → Semaphore
something happened    → Event
state became true     → Condition
everyone must arrive  → Barrier
recursive mutex       → RLock
```

---

# Interview Mental Checklist

When you see a multithreading problem, ask:

1. **What threads exist?**
2. **What shared state exists?**
3. **What ordering is required?**
4. **Is this mutual exclusion or signaling?**
5. **Could a thread wait forever?**
6. **Could two threads deadlock?**
7. **Can the synchronization primitive be simpler?**

---

# Imports to Remember

```python
import threading

threading.Thread
threading.Lock
threading.RLock
threading.Semaphore
threading.BoundedSemaphore
threading.Event
threading.Condition
threading.Barrier
```

---

# Short Mental Summary

```text
Lock        = one thread
RLock       = one thread, recursively
Semaphore   = N permits
Event       = boolean signal
Condition   = wait for shared state
Barrier     = everyone meet here
```

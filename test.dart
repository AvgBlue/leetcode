List<int> array = List.filled(4, 0);
int base = 3;
int max = 5;

void add1(int index) {
  if (index == array.length) return;
  if (array[index] < base - 1 &&
      array.reduce((value, element) => value + element) <= max) {
    array[index]++;
    return;
  }
  array[index] = 0;
  add1(index + 1);
}

void main() {
  for (int i = 0; i < 100; i++) {
    if (array.reduce((value, element) => value + element) == max) print(array);
    add1(0);
  }
}

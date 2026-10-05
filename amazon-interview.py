
# Golden configuration (expected)
golden_config = [
    {
        'card_id': 'hw001234abcd',
        'card_type': 'network-adapter',
        'devices': [
            {
                'device_addr': {'bus': 1, 'slot': 0, 'domain': 1, 'func': 0},
                'device_id': 96,
                'vendor_id': 4567,
                'device_type': 'ethernet',
                'max_queues': 256,
                'driver_version': '1.2.3',
                'firmware_version': '2.1.0'
            },
            {
                'device_addr': {'bus': 0, 'slot': 0, 'domain': 1, 'func': 0},
                'device_id': 512,
                'vendor_id': 4567,
                'device_type': 'bridge',
                'max_queues': 0,
                'driver_version': '1.0.0',
                'firmware_version': '1.5.2'
            },
            {
                'device_addr': {'bus': 13, 'slot': 31, 'domain': 1, 'func': 6},
                'device_id': 60463,
                'vendor_id': 4567,
                'device_type': 'storage',
                'max_queues': 64,
                'driver_version': '3.1.1',
                'firmware_version': '4.0.1'
            }
        ]
    }
]

# Current configuration (actual)
current_config = [
    {
        'card_id': 'hw001234abcd',
        'card_type': 'network-adapter',
        'devices': [
            {
                'device_addr': {'bus': 1, 'slot': 0, 'domain': 1, 'func': 0},
                'device_id': 96,
                'vendor_id': 4567,
                'device_type': 'ethernet',
                'max_queues': 128,  # Different from golden
                'driver_version': '1.2.4',  # Different from golden
                'firmware_version': '2.1.0'
            },
            {
                'device_addr': {'bus': 0, 'slot': 0, 'domain': 1, 'func': 0},
                'device_id': 512,
                'vendor_id': 4567,
                'device_type': 'bridge',
                'max_queues': 0,
                'driver_version': '1.0.0',
                'firmware_version': '1.5.2'
            }
            # Missing storage device from golden config
        ]
    }
]

def get_device_id(card,device):
    result={
                'card_id': card['card_id'],
                'device_addr': device['device_addr'],
                'device_id': device['device_id']
            }
    return result

def is_equal_device(device1,device2):
    is_id= device1['device_id']==device2['device_id']
    return is_id


def is_device_in_config(card,device,config):
    for card_config in config:
        if card_config['card_id']==card['card_id']:
            devices_config=card_config['devices']
            for device_config in devices_config:
                if is_equal_device(device_config,device):
                    return device_config
    return None

    
    

def compare_configurations(golden, current):
    """
    Compare golden and current configurations and return differences.

    Args:
        golden: List of golden configuration dictionaries
        current: List of current configuration dictionaries

    Returns:
        Dictionary containing:
        - missing_devices: Devices in golden but not in current
        - extra_devices: Devices in current but not in golden
        - modified_devices: Devices with different properties
    """
    result= {
    'missing_devices': [],
    'extra_devices': [],
    'modified_devices': []}

    len_golden=len(golden)
    len_current=len(current)

    # fill the missing
    missing_list=[]
    for card_i,card in enumerate(golden):
        devices=card['devices']
        for device in devices:
            if not is_device_in_config(card,device,current):
                missing_list.append(get_device_id(card,device))

    #fill the extra
    
    extra_list=[]
    for card_i,card in enumerate(current):
        devices=card['devices']
        for device in devices:
            if not is_device_in_config(card,device,golden):
                extra_list.append(get_device_id(card,device)) 
    

    #fill the modified

    modified_list=[]
    for card_i,card in enumerate(golden):
        devices=card['devices']
        for device in devices:
            device_in_current=is_device_in_config(card,device,current)
            if device_in_current:
                to_add={
                            'card_id': card['card_id'],
                            'device_addr': device_in_current['device_addr'],
                            'differences': {}
                        }
                differences_list={}

                


                if differences_list:
                    to_add['differences']=differences_list
                    modified_list.append(to_add)

    result['missing_devices']=missing_list
    result['extra_devices']=extra_list
    result['modified_devices']=modified_list
    


    return result


###################
###################

# Expected output format:
expected_result = {
    'missing_devices': [
        {
            'card_id': 'hw001234abcd',
            'device_addr': {'bus': 13, 'slot': 31, 'domain': 1, 'func': 6},
            'device_id': 60463
        }
    ],
    'extra_devices': [],
    'modified_devices': [
        {
            'card_id': 'hw001234abcd',
            'device_addr': {'bus': 1, 'slot': 0, 'domain': 1, 'func': 0},
            'differences': {
                'max_queues': {'golden': 256, 'current': 128},
                'driver_version': {'golden': '1.2.3', 'current': '1.2.4'}
            }
        }
    ]
}

if __name__ == "__main__":
    result = compare_configurations(golden_config, current_config)
    print("Configuration Comparison Result:")
    print(f"Missing devices: {len(result['missing_devices'])}")
    print(f"Extra devices: {len(result['extra_devices'])}")
    print(f"Modified devices: {len(result['modified_devices'])}")
    
    assert result == expected_result

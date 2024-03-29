#
#  iBootLoader | ibootloader
#  structs.py
#
#  This loads struct definitions i've created into IDA
#
#  This file is part of iBootLoader. iBootLoader is free software that
#  is made available under the MIT license. Consult the
#  file "LICENSE" that is distributed together with this file
#  for the exact licensing terms.
#
#  Copyright (c) kat 2021.
#

import idaapi

from disassembler_api.api import API, Struct, Field


class StructLoader:
    def __init__(self, api: API):

        struct = Struct("syscfg_wpcl", [])
        struct.fields.append(Field('version', idaapi.FF_DWORD, 4))
        struct.fields.append(Field('red', idaapi.FF_DWORD, 4))
        struct.fields.append(Field('green', idaapi.FF_DWORD, 4))
        struct.fields.append(Field('blue', idaapi.FF_DWORD, 4))
        api.add_struct(struct)

        struct = Struct("usb_device_request", [])
        struct.fields.append(Field('bmRequestType', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bRequest', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('wValue', idaapi.FF_WORD, 2))
        struct.fields.append(Field('wIndex', idaapi.FF_WORD, 2))
        struct.fields.append(Field('wLength', idaapi.FF_WORD, 2))
        api.add_struct(struct)

        struct = Struct("usb_device_descriptor", [])
        struct.fields.append(Field('bLength', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bDescriptorType', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bcdUSB', idaapi.FF_WORD, 2))
        struct.fields.append(Field('bDeviceClass', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bDeviceSubClass', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bDeviceProtcol', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bDeviceMaxPacketSize0', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('idVendor', idaapi.FF_WORD, 2))
        struct.fields.append(Field('idProduct', idaapi.FF_WORD, 2))
        struct.fields.append(Field('bcdDevice', idaapi.FF_WORD, 2))
        struct.fields.append(Field('iManufacturer', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('iProduct', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('iSerialNumber', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bNumConfigurations', idaapi.FF_BYTE, 1))
        api.add_struct(struct)

        struct = Struct("usb_configuration_descriptor", [])
        struct.fields.append(Field('bLength', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bDescriptorType', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('wTotalLength', idaapi.FF_WORD, 2))
        struct.fields.append(Field('bNumInterfaces', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bConfigurationValue', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('iConfiguration', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bmAttributes', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bMaxPower', idaapi.FF_BYTE, 1))
        api.add_struct(struct)

        struct = Struct("usb_interface_descriptor", [])
        struct.fields.append(Field('bLength', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bDescriptorType', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bInterfaceNumber', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bAlternateSetting', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bNumEndpoints', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bInterfaceClass', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bInterfaceSubClass', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bInterfaceProtocol', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('iInterface', idaapi.FF_BYTE, 1))
        api.add_struct(struct)

        struct = Struct("usb_endpoint_descriptor", [])
        struct.fields.append(Field('bLength', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bDescriptorType', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bEndpointAddress', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bmAttributes', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('wMaxPacketSize', idaapi.FF_WORD, 2))
        struct.fields.append(Field('bInterval', idaapi.FF_BYTE, 1))
        api.add_struct(struct)

        struct = Struct("usb_string_descriptor", [])
        struct.fields.append(Field('bLength', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bDescriptorType', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('wData', idaapi.FF_BYTE, 2))
        api.add_struct(struct)

        struct = Struct("usb_device_qualifier_descriptor", [])
        struct.fields.append(Field('bLength', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bDescriptorType', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bcdUSB', idaapi.FF_WORD, 2))
        struct.fields.append(Field('bDeviceClass', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bDeviceSubClass', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bDeviceProtocol', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bMaxPacketSize0', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bNumConfigurations', idaapi.FF_BYTE, 1))
        struct.fields.append(Field('bReserved', idaapi.FF_BYTE, 1))
        api.add_struct(struct)

        usb_interface_instance = Struct("usb_interface_instance", [])
        usb_interface_instance.fields.append(Field('interface_request_handler', idaapi.FF_DWORD, 4))
        usb_interface_instance.fields.append(Field('non_setup_data_phase_finished_callback', idaapi.FF_DWORD, 4))
        usb_interface_instance.fields.append(Field('activate_interface', idaapi.FF_DWORD, 4))
        usb_interface_instance.fields.append(Field('bus_reset_handler', idaapi.FF_DWORD, 4))
        usb_interface_instance.fields.append(Field('get_interface_handler', idaapi.FF_DWORD, 4))
        usb_interface_instance.fields.append(Field('set_interface_handler', idaapi.FF_DWORD, 4))
        api.add_struct(usb_interface_instance)

        usb_device_io_request = Struct("usb_device_io_request", [])
        usb_device_io_request.fields.append(Field('endpoint', idaapi.FF_DWORD, 4))
        usb_device_io_request.fields.append(Field('io_buffer', idaapi.FF_DWORD, 4))
        usb_device_io_request.fields.append(Field('status', idaapi.FF_DWORD, 4))
        usb_device_io_request.fields.append(Field('io_length', idaapi.FF_DWORD, 4))
        usb_device_io_request.fields.append(Field('return_count', idaapi.FF_DWORD, 4))
        usb_device_io_request.fields.append(Field('callback', idaapi.FF_DWORD, 4))
        usb_device_io_request.fields.append(Field('next', idaapi.FF_DWORD, 4))
        api.add_struct(usb_device_io_request)

        struct = Struct("usb_endpoint_instance", [])
        struct.fields.append(Field('endpoint_address', idaapi.FF_DWORD, 4))
        struct.fields.append(Field('max_packet_size', idaapi.FF_DWORD, 4))
        struct.fields.append(Field('attributes', idaapi.FF_DWORD, 4))
        struct.fields.append(Field('bInterval', idaapi.FF_DWORD, 4))
        struct.fields.append(Field('transfer_size', idaapi.FF_DWORD, 4))
        struct.fields.append(Field('packet_count', idaapi.FF_DWORD, 4))
        struct.fields.append(Field('next_ep', idaapi.FF_DWORD, 4))
        struct.fields.append(Field('io_head', idaapi.FF_DWORD, 4))
        struct.fields.append(Field('io_tail', idaapi.FF_DWORD, 4))
        struct.fields.append(Field('tx_fifo_number', idaapi.FF_DWORD, 4))
        api.add_struct(struct)

        struct = Struct("listentry", [])
        struct.fields.append(Field('cb_id', idaapi.FF_DWORD, 4))
        struct.fields.append(Field('port', idaapi.FF_DWORD, 4))
        struct.fields.append(Field('callback', idaapi.FF_DWORD, 4))
        struct.fields.append(Field('next', idaapi.FF_DWORD, 4))
        api.add_struct(struct)

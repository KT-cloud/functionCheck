import CloudStack

# Lib Setting
api = 'http://10.12.246.44:8080/client/api'
apikey = 'WCvvfpK1LuzdLxPEAHxheG0IVCIzNHdVRsNlT078kb5kg9yWutlBmF4atoDmA04pVsFyO8IiwpMINEtr-vEfnQ'
secret = 'LQWzMyPSycLcJ4rR1dfqbnlJ5hx8v9ylr18toNgC3FpjDERmN7Qs6PYZDOX8BpPISpCbF03PdAAxcs_452GhSA'

cloudstack = CloudStack.Client(api, apikey, secret)

if __name__ == "__main__" :

    vm_id = '' # input vm id
    ser_id = '' # input service offering id

    # VM Scale in/out
    cloudstack.stopVirtualMachine({"id": vm_id})
    cloudstack.changeServiceForVirtualMachine({"id": vm_id, "serviceofferingid":tar_ofr_ID})

    tar_vms = cloudstack.listVirtualMachines({"id":tar_vm_ID})


import CloudStack

# Lib Setting
api = 'http://10.12.246.44:8080/client/api'
apikey = 'WCvvfpK1LuzdLxPEAHxheG0IVCIzNHdVRsNlT078kb5kg9yWutlBmF4atoDmA04pVsFyO8IiwpMINEtr-vEfnQ'
secret = 'LQWzMyPSycLcJ4rR1dfqbnlJ5hx8v9ylr18toNgC3FpjDERmN7Qs6PYZDOX8BpPISpCbF03PdAAxcs_452GhSA'

cloudstack = CloudStack.Client(api, apikey, secret)

if __name__ == "__main__" :
    vms = cloudstack.listVirtualMachines() # VM LIST
    ser_ofrs = cloudstack.listServiceOfferings() # Service Offering LIST

    print "\n============== VM LIST =============="
    for vm in vms :
        print "%s %s %s" % (vm['id'], vm['name'], vm['state'])

    print "\n============== SER OFR LIST ========="
    for ofr in ser_ofrs :
        print "%s %s" % (ofr['id'], ofr['name'])

    print "\n============== FUNC ============="
    vm_name = raw_input("Target VM Name : ")
    ser_name = raw_input("Target Service Offering Name : ")

    print "\n============== Input Confirm ============"
    tar_vm_ID = ''
    tar_ofr_ID = ''

    # Get Taget VM id (tar_vm_ID)
    for vm in vms :
        if vm['name'] == vm_name :
            print "VM : %s %s" % (vm['id'], vm['name'])
            tar_vm_ID = vm['id']

    # Get Target Service Offering id (tar_ofr_ID)
    for ofr in ser_ofrs :
        if ofr['name'] == ser_name :
            print "Service : %s %s" % (ofr['id'], ofr['name'])
            tar_ofr_ID = ofr['id']

    # Start VM Scale in/out
    print "\n============== Processing =============="

    tar_vms = cloudstack.listVirtualMachines({"id":tar_vm_ID})

    # Original VM Info
    for tar_vm in tar_vms :
        print "Before VM's Memory : %s" % (tar_vm['memory'])
        print "Before VM's CPUSpeed : %s" % (tar_vm['cpuspeed'])
        print "Before VM's CPUNumber : %s" % (tar_vm['cpunumber'])
        print "Before VM's Service Offering Name : %s" % (tar_vm['serviceofferingname'])

    # VM Scale in/out
    cloudstack.stopVirtualMachine({"id":tar_vm_ID})
    cloudstack.changeServiceForVirtualMachine({"id":tar_vm_ID, "serviceofferingid":tar_ofr_ID})

    tar_vms = cloudstack.listVirtualMachines({"id":tar_vm_ID})

    # Changed VM Info
    for tar_vm in tar_vms :
        print "\nAfter VM's Memory : %s" % (tar_vm['memory'])
        print "After VM's CPUSpeed : %s" % (tar_vm['cpuspeed'])
        print "After VM's CPUNumber : %s" % (tar_vm['cpunumber'])
        print "After VM's Service Offering Name : %s" % (tar_vm['serviceofferingname'])

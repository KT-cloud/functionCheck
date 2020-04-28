import CloudStack
from time import sleep

# Lib Setting
api = 'http://10.12.246.44:8080/client/api'
apikey = 'WCvvfpK1LuzdLxPEAHxheG0IVCIzNHdVRsNlT078kb5kg9yWutlBmF4atoDmA04pVsFyO8IiwpMINEtr-vEfnQ'
secret = 'LQWzMyPSycLcJ4rR1dfqbnlJ5hx8v9ylr18toNgC3FpjDERmN7Qs6PYZDOX8BpPISpCbF03PdAAxcs_452GhSA'

cloudstack = CloudStack.Client(api, apikey, secret)

if __name__ == "__main__" :
    vms = cloudstack.listVirtualMachines() # VM LIST
    vols = cloudstack.listVolumes() # Volume LIST

    print "\n============== VM LIST =============="
    for vm in vms :
        print "%s %s" % (vm['id'], vm['name'])

    print "\n============== Volume LIST ========="
    for vol in vols :
        print "%s %s" % (vol['id'], vol['name'])

    print "\n============== FUNC SELECT ========="
    print "1 : Volume attach 2 : Volume detach"
    opt = raw_input("Enter : ")

    # Volume Attach
    if opt == "1" :
        print "\n============== Attach ============="
        vm_name = raw_input("Target VM Name : ")
        vol_name = raw_input("Target Volume Name : ")
        print "\n============== Input Confirm ============"
        tar_vm_ID = ''
        tar_vol_ID = ''

        # Get Target VM ID (tar_vm_ID)
        for vm in vms :
            if vm['name'] == vm_name :
                print "VM : %s %s" % (vm['id'], vm['name'])
                tar_vm_ID = vm['id']

        # Get Target Volume ID (tar_vol_ID)
        for vol in vols :
            if vol['name'] == vol_name :
                print "Volume : %s %s" % (vol['id'], vol['name'])
                tar_vol_ID = vol['id']

        # Start Volume Attach
        print "\n============== Processing =============="
        tar_vols = cloudstack.listVolumes({"id": tar_vol_ID})

        # Original Volume Info
        for tar_vol in tar_vols:
            try:
                print "Before Volume's VM : %s" % (tar_vol['vmname'])
            except KeyError:
                print "Before Volume's VM : None"

        cloudstack.attachVolume({"id": tar_vol_ID, "virtualmachineid": tar_vm_ID})
        sleep(2)

        tar_vols = cloudstack.listVolumes({"id": tar_vol_ID})

        # Attached Volume Info
        for tar_vol in tar_vols :
            try :
                print "\nAfter Volume's VM : %s ! Attach Success" % (tar_vol['vmname'])
            except KeyError :
                print "\nAttach Fail"

    else :
        print "\n================= Detach ================"
        vol_name = raw_input("Target Volume Name : ")

        print "\n============== Input Confirm ============"
        tar_vol_ID = ''

        for vol in vols :
            if vol['name'] == vol_name :
                print "Volume : %s %s" % (vol['id'], vol['name'])
                tar_vol_ID = vol['id']

        print "\n============== Processing =============="

        # Original Volume Info
        tar_vols = cloudstack.listVolumes({"id": tar_vol_ID})
        for tar_vol in tar_vols :
            try:
                print "Before Volume's VM : %s" % (tar_vol['vmname'])
            except KeyError:
                print "Before Volume's VM : None"

        cloudstack.detachVolume({"id": tar_vol_ID})
        sleep(1)

        # Detached Volume Info
        tar_vols = cloudstack.listVolumes({"id": tar_vol_ID})
        for tar_vol in tar_vols:
            try:
                print "\nAfter Volume's VM : %s" % (tar_vol['vmname'])
            except KeyError:
                print "\nAfter Volume's VM : None ! detatch Success"


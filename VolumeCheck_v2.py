import CloudStack
from time import sleep

# Lib Setting
api = 'http://10.12.246.44:8080/client/api'
apikey = 'WCvvfpK1LuzdLxPEAHxheG0IVCIzNHdVRsNlT078kb5kg9yWutlBmF4atoDmA04pVsFyO8IiwpMINEtr-vEfnQ'
secret = 'LQWzMyPSycLcJ4rR1dfqbnlJ5hx8v9ylr18toNgC3FpjDERmN7Qs6PYZDOX8BpPISpCbF03PdAAxcs_452GhSA'

cloudstack = CloudStack.Client(api, apikey, secret)

if __name__ == "__main__" :

    vol = cloudstack.createVolume()

    vol_id = vol['id']
    vm_id = '' # input vm id

    cloudstack.attachVolume({"id": vol_id, "virtualmachineid": vm_id})
    sleep(2)

    tar_vols = cloudstack.listVolumes({"id": vol_id})

    # Attached Volume Info
    for tar_vol in tar_vols :
        try :
            print "\n[%s] Attach Success" % (tar_vol['vmname'])
        except KeyError :
            print "\nAttach Fail"

    cloudstack.detachVolume({"id": vol_id})
    sleep(2)

    # Detached Volume Info
    tar_vols = cloudstack.listVolumes({"id": vol_id})
    for tar_vol in tar_vols:
        try:
            print "\n[%s] detatch Fail" % (tar_vol['vmname'])
        except KeyError:
            print "detatch Success"


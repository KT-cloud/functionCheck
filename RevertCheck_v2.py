import CloudStack

api = 'http://10.12.246.44:8080/client/api'
apikey = 'WCvvfpK1LuzdLxPEAHxheG0IVCIzNHdVRsNlT078kb5kg9yWutlBmF4atoDmA04pVsFyO8IiwpMINEtr-vEfnQ'
secret = 'LQWzMyPSycLcJ4rR1dfqbnlJ5hx8v9ylr18toNgC3FpjDERmN7Qs6PYZDOX8BpPISpCbF03PdAAxcs_452GhSA'

cloudstack = CloudStack.Client(api, apikey, secret)

if __name__ == "__main__" :

    vol_id = '' # input volume id
    snp_name = 'automation_test'
    vol_name = 'automation_test'

    cloudstack.createSnapshot({"volumeid":vol_id, "name":snp_name})
    snps = cloudstack.listSnapshots()
    snp_id = ''

    # Snapshot Create Check (idx)
    idx = 0
    for snp in snps :
        if snp['name'] == snp_name :
            idx = 1
            snp_id = snp['id']

    if idx == 1 :
        print "Snapshot Create Success"
    else :
        print "Snapshot Create Fail"

    cloudstack.createVolume({"snapshotid":snp_id, "name":vol_name})

    vols = cloudstack.listVolumes()
    idx = 0

    for vol in vols :
        if vol['name'] == vol_name :
            idx = 1

    if idx == 1 :
        print "Volume Revert Success"
    else :
        print "Volume Revert Fail"
    
    cloudstack.deleteVolume({"id":vol_id})
    cloudstack.deleteSnapshot({"id":snp_id})

import CloudStack

api = 'http://10.12.246.44:8080/client/api'
apikey = 'WCvvfpK1LuzdLxPEAHxheG0IVCIzNHdVRsNlT078kb5kg9yWutlBmF4atoDmA04pVsFyO8IiwpMINEtr-vEfnQ'
secret = 'LQWzMyPSycLcJ4rR1dfqbnlJ5hx8v9ylr18toNgC3FpjDERmN7Qs6PYZDOX8BpPISpCbF03PdAAxcs_452GhSA'

cloudstack = CloudStack.Client(api, apikey, secret)

if __name__ == "__main__" :
    vols = cloudstack.listVolumes() # VM LIST
    snps = cloudstack.listSnapshots() # Snapshot LIST

    print "\n============== Volume LIST =============="
    for vol in vols :
        print "%s %s" % (vol['id'], vol['name'])

    print "\n============== Snapshot LIST ==========="
    for snp in snps :
        print "%s %s %s" % (snp['id'], snp['name'], snp['volumename'])

    print "\n============== FUNC ============="
    vol_name = raw_input("Target Volume Name : ")
    snp_name = raw_input("Created Snapshot Name : ")

    print "\n============== Input Confirm ============"
    tar_vol_ID = ''
    for vol in vols :
        if vol['name'] == vol_name :
            print "Volume : %s %s" % (vol['id'], vol['name'])
            tar_vol_ID = vol['id']

    print "\n============== Processing =============="
    cloudstack.createSnapshot({"volumeid":tar_vol_ID, "name":snp_name})
    snps = cloudstack.listSnapshots()
    snp_ID = ''

    # Snapshot Create Check (idx)
    idx = 0
    for snp in snps :
        if snp['name'] == snp_name :
            idx = 1
            snp_ID = snp['id']
        print "Snapshot Name : %s " % (snp['name'])

    if idx == 1 :
        print "**** Snapshot Create Success ! ****"
    else :
        print "**** Snapshot Create Fail ****"

    ''' Volume Delete (431 Error)
    cloudstack.detachVolume({"id":tar_vol_ID})
    cloudstack.deleteVolume({"id":tar_vol_ID})
    vols = cloudstack.listVolumes()
    
    idx = 0
    for vol in vols :
    if vol['id'] == tar_vol_ID :
    print "\n**** Volume Delete Fail ****"
    idx = 1
    
    if idx == 0 :
    print "\n**** Volume Delete Success! ****"
    
    '''

    # Revert Volume Check(idx)
    vol_name = raw_input("\n Reverted Volume Name : ")
    cloudstack.createVolume({"snapshotid":snp_ID, "name":vol_name})

    vols = cloudstack.listVolumes()
    idx = 0

    print "\n~~~~~~~~~~ Volume List ~~~~~~~~~~~"
    for vol in vols :
        if vol['name'] == vol_name :
            idx = 1
        print "vol name : %s" % (vol['name'])
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    if idx == 1 :
        print "\n**** Volume Revert Success ****!"
    else :
        print "\n**** Volume Revert Fail ****"
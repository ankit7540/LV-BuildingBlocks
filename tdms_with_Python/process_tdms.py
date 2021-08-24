
'''
Module to :
           ) list groups and channels in tdms file
		   ii) extract a particular channel to a numpy array
		        or export it to a file
		   
'''


# requirements : numpy 
#                nptdms



import nptdms
import pandas as pd


#######################################################

def get_tdms_info(file):

	'''
	Function to list the groups and channels available in 
	a TDMS file 
	'''
    
    # load file
    tdms_file = nptdms.TdmsFile( file )
    

    groups_data = tdms_file.groups()
    #print(groups_data, type(groups_data))

    for i in range(len(groups_data)):
        print('')
        print('\t gr',i, groups_data[i])
        
        present_gr = groups_data[i]
        
        channels_data = present_gr.channels()
        
        for j in range(len(channels_data)):
            print("\t\t\t  ch", j, channels_data[j])
        
        

#######################################################


def get_tdms_data(file, group_index, ch_index , export=None):
    '''
    

    Parameters
    ----------
    file : string
        FILE PATH.
        
    group_index : integer
        index for the group
        
    ch_index : integer
        index for the group
        
    export : string
        export the data

    Returns
    -------
    data as np array

    '''
    
    # load file
    tdms_file = nptdms.TdmsFile( file )
    
    
    # show groups
    groups_data = tdms_file.groups()
    
    group = groups_data[group_index]
    print('\n\tgroup name : ', group.name )

    group_selected = tdms_file[group.name]
    chList = group_selected.channels()
    
    ch = chList[ch_index]
    
    print('\tch name : ', ch.name )
    
    data_ch =  tdms_file[group.name][ch.name]
    
    print('\t datatype : ',type(data_ch.data), ', dimension : ', data_ch.data.shape )
    
    # temporal analysis
    time = data_ch.time_track()
    
    prop = data_ch.properties
    
    print('\t----- PROPERTIES ------ ')
    for key, value in prop.items():
        print('\t\t',key, " : ", value )

    print( '\t\t Read dt : ', time[1]-time[0], ' sec', ' | sample rate (Hz) : ', round(1/time[1]-time[0],1))
    print('\t\t type : ', data_ch.data.dtype)    
    print('\t ---------------------------------------\n')
    
    print('\t Metadata')
    s = tdms_file.properties
    for key, value in s.items():
        print('\t\t', key, ' : ', value)
        
        
    if export != None :
        print('\n\t Exporting to >> ', export )        
        df = pd.DataFrame(data=data_ch.data)
        
        # export as csv
        df.to_csv( export, sep='\t')
        
        print('\t\t   done.')
    else:
        print('\t\t   done.')
    
    #########################################################
    
    
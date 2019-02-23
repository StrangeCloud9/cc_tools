import cc_dat_utils
import cc_data
import json
def json2dat(json_data): 
    dic_data = json.loads(json_data) 
    ccdata = cc_data.CCDataFile() 
    for level_dic in dic_data: 
        cclevel = cc_data.CCLevel() 
        #set non-field value
        cclevel.level_number = level_dic['level_number'] 
        cclevel.time = level_dic['time'] 
        cclevel.num_chips = level_dic['num_chips'] 
        cclevel.upper_layer = level_dic['upper_layer'] 
        cclevel.lower_layer = level_dic['lower_layer']
        
        #set optional field
        if "monsters" in level_dic:
            monsters = []
            for x_y in level_dic["monsters"]:
                coord = cc_data.CCCoordinate(x_y[0], x_y[1])
                monsters.append(coord)
            monsters_field = cc_data.CCMonsterMovementField(monsters)
            cclevel.add_field(monsters_field)
        if "traps" in level_dic:
            trap_controls = []
            for i in range(len(level_dic["traps"])):
                trap_control = cc_data.CCTrapControl(level_dic["controls"][i][0],level_dic["controls"][i][1],level_dic["traps"][i][0],level_dic["traps"][i][1])
                trap_controls.append(trap_control)
            trap_controls_field = cc_data.CCTrapControlsField(trap_controls)
            cclevel.add_field(trap_controls_field)
        if "clone_machine" in level_dic:
            clones = []
            for i in range(len(level_dic["clone_machine"])):
                clone = cc_data.CCCloningMachineControl(level_dic["clone_button"][i][0], level_dic["clone_button"][i][1], level_dic["clone_machine"][i][0], level_dic["clone_machine"][i][1])
                clones.append(clone)
            clones_field = cc_data.CCCloningMachineControlsField(clones)
            cclevel.add_field(clones_field)

        #set necessary field
        map_title_field = cc_data.CCMapTitleField(level_dic['map_title']) 
        map_hint_field = cc_data.CCMapHintField(level_dic['map_hint']) 
        encoded_password_field = cc_data.CCEncodedPasswordField(level_dic['encoded_password'])

        cclevel.add_field(map_title_field)
        cclevel.add_field(map_hint_field)
        cclevel.add_field(encoded_password_field)
        #add level to ccdata
        ccdata.add_level(cclevel)
    return ccdata
#Part 3
#Load your custom JSON file
json_data = (open('data/bwang2_cc1.json','r').read()) 
#Convert JSON data to cc_data
ccdata = json2dat(json_data) 
#Save converted data to DAT file
dat_file_name = 'data/bwang2_cc1.dat' 
cc_dat_utils.write_cc_data_to_dat(ccdata, dat_file_name)
import json

def makeJson(infos):
    # set for space to make json
    EntireCourses = {}
    ASUcourses = []
    entire = {}
    courses = []
    start = 1

    for row in infos:
        # cluster courses by subject
        if start == 1:
            temp = row[0]
            start = 0
        
        if temp != row[0]:
            entire["subject"] = temp
            entire["courses"] = courses
            ASUcourses.append(entire)
            temp = row[0]
            courses = []
            entire = {}
            
        desc = {}

        # course identifier
        desc["code"] = row[1]
        desc["name"] = row[2]

        # course topic
        desc["topic"] = row[3]

        # requirements for different programs
        if row[5] == "1":
            desc["coreCSmajor"] = True
        if row[6] == "1":
            desc["reqCSminor"] = True
        if row[7] == "1":
            desc["eltCSminor"] = True
        if row[8] == "1":
            desc["coreCYmajor"] = True
        if row[9] == "1":
            desc["reqCSminor"] = True
        if row[10] == "1":
            desc["eltCYminor"] = True



        # not offered currently
        if row[14] == "TRUE":
            desc["unavailable"] = True
        # course availiability
        else:
            availtmp = []
            if row[15] == "O":
                availtmp.append("Fall")
            if row[16] == "O":
                availtmp.append("Spring")
            if row[17] == "O":
                availtmp.append("Summer")
            desc["availsemester"] = availtmp
        
        # AND prerequisites (X consideration on passing grade)
        ANDtmp = []
        for i in [18,20,22,24]:
            if row[i] != "":
                ANDtmp.append(row[i])
            else:
                pass

        if len(ANDtmp) != 0:
            desc["prereq"] = ANDtmp

        # OR prerequisites
        if row[28] and row[30]:
            desc["prereq(OR)"] = [row[28], row[30]]

        # prestanding, preapproval
        if row[26] != "":
            desc["prestandings"] = row[26]
        if row[27] == "O":
            desc["preapproval"] = True

        courses.append(desc)

    # Last step    
    entire["subject"] = temp
    entire["courses"] = courses
    ASUcourses.append(entire)
    courses = []
    entire = {}

    # bind it to one
    EntireCourses["ASUcourses"] = ASUcourses

    # create json file
    with open(f"data\coursejson\courses_info.json", "w", encoding="utf-8") as f:
        json.dump(EntireCourses, f, indent=4, ensure_ascii=False)
            

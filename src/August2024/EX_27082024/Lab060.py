My_shpping_list = ["cloths", "snakes", "glossary"]
print(My_shpping_list[1])
print(len(My_shpping_list))


def more_item(My_list):
    #My_list.append("shoes")
    #My_list.remove("snakes")
    My_list.insert(1, "shoes")
    return My_list

p = more_item(My_shpping_list)
print(p)

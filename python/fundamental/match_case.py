# underscore -> for default case

# Traffic Light 

color = input("enter color :")

match color:                  # on which variale ->  to apply condition 
    case "Green":
        print("Go")
    case "Yellow":
        print("Look")
    case "Red":
        print("Stop")
    case _:                   # _   -> for default case
        print("wrong color")

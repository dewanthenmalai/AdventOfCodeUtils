def parse_input(puzzle1_handler, puzzle2_handler, puzzle=1, test=False, style="line"):
    filename = ""
    if test:
        filename = "TestInput.txt"
    else:
        filename = "Input.txt"
    
    with open(filename)as f:
        match style:
            case "line":
                input = [line.strip() for line in f]
            case _:
                print(f"Unknown parse style {style}")
                return
    
    match puzzle:
        case 1:
            puzzle1_handler(input)
        case 2:
            puzzle2_handler(input)
        case _:
            print(f"Invalid puzzle {args.puzzle}")
            return
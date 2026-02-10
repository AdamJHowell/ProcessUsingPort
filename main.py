import argparse

import psutil


def get_process_name_by_port( port ):
    """
    Finds the process name listening on the specified port.
    """
    print( f"Searching for process listening on port {port}..." )

    # Iterate over all network connections.
    # kind='inet' covers both IPv4 and IPv6.
    try:
        connections = psutil.net_connections( kind = 'inet' )
    except psutil.AccessDenied:
        print( "[Error] Access Denied. Try running the script as Administrator." )
        return None

    for conn in connections:
        # Check if the port matches and the status is 'LISTEN'.
        if conn.laddr.port == port and conn.status == psutil.CONN_LISTEN:
            pid = conn.pid

            if pid is None:
                # Sometimes system processes/drivers don't expose a PID to userland.
                print( f"Port {port} is in use, but the PID could not be retrieved (System/Kernel)." )
                return None

            try:
                # Get the process object using the PID.
                process = psutil.Process( pid )
                print( f"Found PID: {pid}" )

                # Return the name (equivalent to Image Name in tasklist).
                return process.name()

            except psutil.NoSuchProcess:
                print( f"Process with PID {pid} no longer exists." )
                return None
            except psutil.AccessDenied:
                print( f"Found PID {pid}, but access to process details was denied." )
                return None

    return None


def main():
    # Setup command line argument parsing.
    parser = argparse.ArgumentParser( description = "Find the Windows executable listening on a specific port." )
    parser.add_argument( "port", type = int, help = "The port number to check (integer)." )

    args = parser.parse_args()

    # Get the result.
    exe_name = get_process_name_by_port( args.port )

    # Output the result.
    if exe_name:
        print( f"Executable: {exe_name}" )
    else:
        print( f"No process found listening on port {args.port}." )


if __name__ == "__main__":
    main()

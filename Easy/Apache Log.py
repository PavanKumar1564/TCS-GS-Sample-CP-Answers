# Problem Name is &&& ApacheLog &&& PLEASE DO NOT REMOVE THIS LINE. 
"""
Instructions to candidate. 
1) Run this code in the REPL to observe its behaviour. The 
execution entry point is specified at the bottom. 
2) Consider adding some additional tests in do_tests_pass(). 
3) Implement find_top_ip_address() correctly. 
4) If time permits, try to improve your implementation. 
"""
def find_top_ip_address(lines): 
    """ Given an Apache log file, return IP address(es) which accesses the site most often. 
    
    Our log is in this format (Common Log Format). One entry per line and it starts with an IP address which accessed the site, followed by a whitespace.
    
    10.0.0.1 - frank [10/Dec/2000:12:34:56 -0500] "GET /a.gif HTTP/1.0" 200 234 
    
    Log file entries are passed as a list. 
    
    NOTE: In case of tie, this returns a comma-separated list of IP addresses. Tie is not mentioned explicitly in the exercise on purpose. 
    """
    access_list = {} 
    for line in lines: 
        ip_address = line.split()[0] 
        access_list[ip_address] = access_list.get(ip_address, 0) + 1 
    ip_addresses = [key for key, val in access_list.items() 
        if val == max(access_list.values())]
    #print(ip_addresses)
    return ','.join(sorted(ip_addresses)) 
        
def do_tests_pass():
    """Returns True if the test passes. Otherwise returns False.""" 
    tests_passed = True
    lines = ["10.0.0.1 - frank [10/Dec/2000:12:34:56 -0500] \"GET /a.gif HTTP/1.0\" 200 234", 
                        "10.0.0.1 - frank [10/Dec/2000:12:34:57 -0500] \"GET /b.gif HTTP/1.0\" 200 234", 
                        "10.0.0.2 - nancy [10/Dec/2000:12:34:58 -0500] \"GET /c.gif HTTP/1.0\" 200 234" 
                        ]
def do_tests_pass(): 
    """Returns True if the test passes. Otherwise returns False.""" 
                            
    tests_passed = True 
    lines = ["10.0.0.1 - frank [10/Dec/2000:12:34:56 -0500] \"GET /a.gif HTTP/1.0\" 200 234", 
                 "10.0.0.1 - frank [10/Dec/2000:12:34:57 -0500] \"GET /b.gif HTTP/1.0\" 200 234"
                  "10.0.0.2 - nancy [10/Dec/2000:12:34:58 -0500] \"GET /c.gif HTTP/1.0\" 200 234"
                 ]
    result = find_top_ip_address(lines) 
    if result != "10.0.0.1": 
                                
        tests_passed = False 
    #tie case 
    lines = ["10.0.0.1 - frank [10/Dec/2000:12:34:56 -0500] \"GET /a .gif HTTP/1.0\" 200 234", 
                         "10.0.0.1 - frank [10/Dec/2000:12:34:57 -0500] \"GET /b.gif HTTP/1 .0\" 200 234",
                         "10.0.0.2 - nancy [10/Dec/2000:12:34:58 -0500] \"GET /c.gif HTTP/1 .0\" 200 234",
                         "10.0.0.2 - nancy [10/Dec/2000:12:34:59 -0500] \"GET /c.gif HTTP/1 .0\" 200 234", 
                         "10.0.0.3 - logan [10/Dec/2000:12:34:59 -0500] \"GET /d.gif HTTP/1 .0\" 200 234" 
            ]
    result = find_top_ip_address(lines)
    if result != "10.0.0.1,10.0.0.2": 
        tests_passed = False 
    
    if tests_passed: 
        print("test passed") 
                                
    else: 
        print("test failed") 
    return tests_passed 
if __name__ == "__main__":
    do_tests_pass() 


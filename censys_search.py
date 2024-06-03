from censys.search import CensysHosts

ID = "YOUR_API_ID"
SECRET = "YOUR_API_SECRET"

if __name__=="__main__":
	dns = input("Enter domain: ")
	info_list = []
	host = CensysHosts(api_id=ID, api_secret=SECRET)
	result = host.search("dns.names: " + dns, per_page=50, pages=1)()
	for res in result:
		info_list.append({
            "ip": res["ip"],
			"name": res["autonomous_system"]["name"],
            "country": res["location"]["country"],
            "asn": res["autonomous_system"]["asn"]
        })
	for i in info_list:
		for key, value in i.items():
			print("{}: {}".format(key, value))
		print()

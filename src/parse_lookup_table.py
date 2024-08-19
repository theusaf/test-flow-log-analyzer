import csv
from .log_record import LogRecord

# See https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml
protocol_map = {"hopopt": "0", "icmp": "1", "igmp": "2", "ggp": "3", "ipv4": "4", "st": "5", "tcp": "6", "cbt": "7", "egp": "8", "igp": "9", "bbn-rcc-mon": "10", "nvp-ii": "11", "pup": "12", "argus (deprecated)": "13", "emcon": "14", "xnet": "15", "chaos": "16", "udp": "17", "mux": "18", "dcn-meas": "19", "hmp": "20", "prm": "21", "xns-idp": "22", "trunk-1": "23", "trunk-2": "24", "leaf-1": "25", "leaf-2": "26", "rdp": "27", "irtp": "28", "iso-tp4": "29", "netblt": "30", "mfe-nsp": "31", "merit-inp": "32", "dccp": "33", "3pc": "34", "idpr": "35", "xtp": "36", "ddp": "37", "idpr-cmtp": "38", "tp++": "39", "il": "40", "ipv6": "41", "sdrp": "42", "ipv6-route": "43", "ipv6-frag": "44", "idrp": "45", "rsvp": "46", "gre": "47", "dsr": "48", "bna": "49", "esp": "50", "ah": "51", "i-nlsp": "52", "swipe (deprecated)": "53", "narp": "54", "min-ipv4": "55", "tlsp": "56", "skip": "57", "ipv6-icmp": "58", "ipv6-nonxt": "59", "ipv6-opts": "60", "cftp": "62", "sat-expak": "64", "kryptolan": "65", "rvd": "66", "ippc": "67", "sat-mon": "69", "visa": "70", "ipcv": "71", "cpnx": "72", "cphb": "73", "wsn": "74", "pvp": "75", "br-sat-mon": "76",
                "sun-nd": "77", "wb-mon": "78", "wb-expak": "79", "iso-ip": "80", "vmtp": "81", "secure-vmtp": "82", "vines": "83", "iptm": "84", "nsfnet-igp": "85", "dgp": "86", "tcf": "87", "eigrp": "88", "ospfigp": "89", "sprite-rpc": "90", "larp": "91", "mtp": "92", "ax.25": "93", "ipip": "94", "micp (deprecated)": "95", "scc-sp": "96", "etherip": "97", "encap": "98", "gmtp": "100", "ifmp": "101", "pnni": "102", "pim": "103", "aris": "104", "scps": "105", "qnx": "106", "a/n": "107", "ipcomp": "108", "snp": "109", "compaq-peer": "110", "ipx-in-ip": "111", "vrrp": "112", "pgm": "113", "l2tp": "115", "ddx": "116", "iatp": "117", "stp": "118", "srp": "119", "uti": "120", "smp": "121", "sm (deprecated)": "122", "ptp": "123", "isis over ipv4": "124", "fire": "125", "crtp": "126", "crudp": "127", "sscopmce": "128", "iplt": "129", "sps": "130", "pipe": "131", "sctp": "132", "fc": "133", "rsvp-e2e-ignore": "134", "mobility header": "135", "udplite": "136", "mpls-in-ip": "137", "manet": "138", "hip": "139", "shim6": "140", "wesp": "141", "rohc": "142", "ethernet": "143", "aggfrag": "144", "nsh": "145"}


def parse_lookup_table(table: str) -> list[LogRecord]:
    reader = csv.DictReader(table.splitlines())
    records = []
    for row in reader:
        tag = row.pop("tag")
        if row["protocol"] in protocol_map:
            row["protocol"] = protocol_map[row["protocol"]]
        record = LogRecord(fields=row, tag=tag)
        records.append(record)
    return records

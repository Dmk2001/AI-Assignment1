import json


def bin_packing_problems():
    class BPPInstance:
        def __init__(self, name, num_weights, bin_size, sizes):
            self.name = name
            self.num_weights = num_weights
            self.bin_size = bin_size
            self.sizes = sizes

    def parse_json(json_data):
        bpp_instances = []
        for bpp_key, bpp_data in json_data.items():
            bpp_data = bpp_data[0]  # Assuming each BPP key has only one entry
            num_weights = bpp_data['num_items']
            bin_size = bpp_data['bin_size']
            sizes_dict = bpp_data['sizes'][0]

            sizes = []
            for weight, count in sizes_dict.items():
                sizes.extend([int(weight)] * count)

            bpp_instances.append(BPPInstance(bpp_key,num_weights, bin_size, sizes))

        return bpp_instances

    # Your JSON data
    file = "Binpacking.json"
    with open(file, "r") as outfile:
        data = json.load(outfile)

    # Parse JSON data
    bpp_objects = parse_json(data)
    return bpp_objects

from lxml import etree

def parse_config(path):
    tree = etree.parse(path)
    objects = []
    for obj in tree.xpath('//MetaDataObject'):
        objects.append({
            'name': obj.get('name'),
            'type': obj.tag,
            'uuid': obj.get('uuid')})
    return objects

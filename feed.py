import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml', 'r') as file:
    yaml_content = yaml.safe_load(file)

    rss_element = xml_tree.Element('rss', {'version':'2.0',
    'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'xmlns:content':'http://purl.org/rss/1.0/modules/content/'})

channel_el = xml_tree.SubElement(rss_element, 'channel')

link_prefix = yaml_content['link']

xml_tree.SubElement(channel_el, 'title').text = yaml_content['title']
xml_tree.SubElement(channel_el, 'format').text = yaml_content['format']
xml_tree.SubElement(channel_el, 'subtitle').text = yaml_content['subtitle']
xml_tree.SubElement(channel_el, 'itunes:author').text = yaml_content['author']
xml_tree.SubElement(channel_el, 'description').text = yaml_content['description']
xml_tree.SubElement(channel_el, 'itunes:image', {'href':link_prefix+yaml_content['image']}) 
xml_tree.SubElement(channel_el, 'language').text = yaml_content['language']
xml_tree.SubElement(channel_el, 'title').text = link_prefix
xml_tree.SubElement(channel_el, 'itunes:category', {'text':yaml_content['category']}) 

for item in yaml_content['item']:
    item_el = xml_tree.SubElement(channel_el, 'item')
    xml_tree.SubElement(item_el, 'itunes:title').text = item['title']
    xml_tree.SubElement(item_el, 'itunes:author').text = yaml_content['author']
    xml_tree.SubElement(item_el, 'description').text = item['description']
    xml_tree.SubElement(item_el, 'itunes:duration').text = item['duration']
    xml_tree.SubElement(item_el, 'pubDate').text = item['published']
    

    enclose_el = xml_tree.SubElement(item_el, 'enclosure', {
        'url': link_prefix + item['file'],
        'type': 'audio/mp3',
        'length': item['length']
    })

output_tree = xml_tree.ElementTree(rss_element)
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)

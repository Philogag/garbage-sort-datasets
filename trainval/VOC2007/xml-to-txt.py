import xml.etree.ElementTree as ET
import glob
import sys
import os

path_to_folder = './xml-to-txt'
#print(path_to_folder)
os.chdir(path_to_folder)


xml_list = glob.glob('*.xml')
if len(xml_list) == 0:
  print("Error: no .xml files found in ground-truth")
  sys.exit()

for tmp_file in xml_list:
  with open(tmp_file.replace(".xml", ".txt"), "w") as new_f:
    root = ET.parse(tmp_file).getroot()
    temp = []
    for obj in root.findall('object'):
      obj_name = obj.find('name').text
      print(type(obj_name))
      print(obj_name)
      name = {"一次性快餐盒": '1', "书籍纸张": '2', '充电宝': '3', '剩饭剩菜': '4',
              '包': '5', '垃圾桶': '6', '塑料器皿': '7', '塑料玩具': '8', '塑料衣架': '9',
              '大骨头': '10', '干电池': '11', '快递纸袋': '12', '插头电线': '13', '旧衣服': '14',
              '易拉罐': '15', '枕头': '16', '果皮果肉': '17', '毛绒玩具': '18', '污损塑料': '19',
              '污损用纸': '20', '洗护用品': '21', '烟蒂': '22', '牙签': '23', '玻璃器皿': '24',
              '砧板': '25', '筷子': '26', '纸盒纸箱': '27', '花盆': '28', '茶叶渣': '29',
              '菜帮菜叶': '30', '蛋壳': '31', '调料瓶': '32', '软膏': '33', '过期药物': '34',
              '酒瓶': '35', '金属厨具': '36', '金属器皿': '37', '金属食品罐': '38', '锅': '39',
              '陶瓷器皿': '40', '鞋': '41', '食用油桶': '42', '饮料瓶': '43', '鱼骨': '44'}
      bndbox = obj.find('bndbox')
      left = bndbox.find('xmin').text
      top = bndbox.find('ymin').text
      right = bndbox.find('xmax').text
      bottom = bndbox.find('ymax').text
      temp.append(left + " " + top + " " + right + " " + bottom + " " + name[obj_name] + '\n')
    temp.reverse()
    for t in temp:
      new_f.write(t)


print("Conversion completed!")
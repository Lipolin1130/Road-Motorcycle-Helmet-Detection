import json
import os

name2id = {'motorcycle': 0, 'helmet': 1, 'person': 2}

def convert(img_size, box):
    dw = 1. /(img_size[0])
    dh = 1. /(img_size[1])
    x = (box[0] + box[2]) / 2.0
    y = (box[1] + box[3]) / 2.0
    w = abs(box[2] - box[0])
    h = abs(box[3] - box[1])
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def decode_json(json_floder_path, txt_outer_path, json_name):
# json_floder_path='E:\\Python_package\\itesjson\\'
# json_name='V1125.json'
    txt_name = txt_outer_path + json_name[:-5] + '.txt'
    with open(txt_name,'w') as f:
        json_path = os.path.join(json_floder_path, json_name) # OS 路徑結合
        data = json.load(open(json_path, 'r', encoding='gb2312',errors='ignore'))
        img_w = data['imageWidth'] #圖片的高
        img_h = data['imageHeight'] #圖片的寬
        isshape_type=data['shapes'][0]['shape_type']
        print(isshape_type)
        #print(isshape_type)
        #print('下方判断根据这里的值可以设置为你自己的类型，我这里是polygon'多边形)
        #len(data['shapes'])
        for i in data['shapes']:
            label_name = i['label'] #得到json中你标记的类名
            if (i['shape_type'] == 'polygon'): #数据类型为多边形 需要转化为矩形
                x_max = 0
                y_max = 0
                x_min = 100000
                y_min = 100000
                for lk in range(len(i['points'])):
                    x1 = float(i['points'][lk][0])
                    y1 = float(i['points'][lk][1])
                    # print(x1)
                    if x_max < x1:
                        x_max = x1
                    if y_max < y1:
                        y_max = y1
                    if y_min > y1:
                        y_min = y1
                    if x_min > x1:
                        x_min = x1
                bb = (x_min, y_max, x_max, y_min)
            if (i['shape_type'] == 'rectangle'): #为矩形不需要转换
                x1 = float(i['points'][0][0])
                y1 = float(i['points'][0][1])
                x2 = float(i['points'][1][0])
                y2 = float(i['points'][1][1])
                bb = (x1, y1, x2, y2)
            bbox = convert((img_w, img_h), bb)
            try:
                f.write(str(name2id[label_name]) + " " + " ".join([str(a) for a in bbox]) + '\n')
            except:
                pass

if __name__ == "__main__":
    json_folder_path = 'D:\Project\Road Motorcycle Helmet Detection\\Temp\Annotations' #存放json的文件夹的绝对路径
    txt_outer_path='D:\Project\Road Motorcycle Helmet Detection\\Temp\YoloLables\\' #存放txt的文件夹绝对路径
    json_names = os.listdir(json_folder_path)
    print("共有：{} 個文件待轉化".format(len(json_names)))
    flagcount = 0
    for json_name in json_names:
        decode_json(json_folder_path, txt_outer_path, json_name)
        flagcount += 1
        print("還剩下{}個文件未轉化".format(len(json_names) - flagcount))
        # break
    # break
    print('轉化全部完畢')
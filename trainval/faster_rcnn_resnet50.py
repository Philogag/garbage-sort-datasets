import cv2
import pandas as pd
import numpy as np
import os
import re

from PIL import Image

import albumentations as A
from albumentations.pytorch.transforms import ToTensorV2

import torch
import torchvision

from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchvision.models.detection import FasterRCNN
from torchvision.models.detection.rpn import AnchorGenerator

from torch.utils.data import DataLoader, Dataset
from torch.utils.data.sampler import SequentialSampler

from matplotlib import pyplot as plt


with open('./dataset/train_data.txt', 'r') as f:
    datas = f.read().split('\n')


class WheatDataset(Dataset):

    def __init__(self, datas, transforms=None):
        super().__init__()

        # self.image_ids = dataframe['image_id'].unique()
        self.datas = datas
        # self.image_dir = image_dir
        self.transforms = transforms

    def __getitem__(self, index: int):
        # image_id = self.image_ids[index]
        # records = self.df[self.df['image_id'] == image_id]
        data = self.datas[index]
        path = data.split()[0]
        bboxs = data.split()[1:]

        image = cv2.imread("../trainval" + path, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
        image /= 255.0

        labels = []
        boxes = []
        for bbox in bboxs:
            boxes.append(list(map(int, bbox.split(',')))[:4])
            labels.append(list(map(int, bbox.split(',')))[4])

        boxes = np.array(boxes, dtype=np.float32)
        labels = torch.from_numpy(np.array(labels, dtype=np.int64))

        area = (boxes[:, 3] - boxes[:, 1]) * (boxes[:, 2] - boxes[:, 0])
        area = torch.as_tensor(area, dtype=torch.float32)

        target = {}
        target['boxes'] = boxes
        target['labels'] = labels
        # target['masks'] = None
        target['image_id'] = torch.tensor([index])
        target['area'] = area
        #         target['iscrowd'] = iscrowd

        if self.transforms:
            sample = {
                'image': image,
                'bboxes': target['boxes'],
                'labels': labels
            }
            sample = self.transforms(**sample)
            image = sample['image']

            target['boxes'] = torch.stack(tuple(map(torch.tensor, zip(*sample['bboxes'])))).permute(1, 0)

        return image, target

    def __len__(self) -> int:
        return len(self.datas)

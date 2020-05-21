import os

def file_name(file_dir, image_file):
    result = open('train.txt', 'w')
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if file == '.DS_Store':
                continue
            f = open("./xml-to-txt/%s" % (file),'r')
            if os.path.splitext(file)[1] == '.txt':
                file_name = file[0:-4]  #去掉.txt
                print(file_name)
            else:
                continue
            read = f.read()
            a = 'b'.join(read.split('\n'))
            a = ','.join(a.split())
            a = ' '.join(a.split('b'))
            a = a[:-1]
            image_file1 = image_file + file_name + '.jpg ' + a + "\n"
            print(image_file1)
            result.writelines(image_file1)


    result.close()

image_file = '/VOC2007/JPEGImages/'

file_name("./xml-to-txt",image_file)

loss_hist = Averager()
itr = 1

for epoch in range(num_epochs):
    loss_hist.reset()

    for images, targets in train_data_loader:

        images = list(image.to(device) for image in images)
        targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

        loss_dict = model(images, targets)

        losses = sum(loss for loss in loss_dict.values())
        loss_value = losses.item()

        loss_hist.send(loss_value)

        optimizer.zero_grad()
        losses.backward()
        optimizer.step()

        if itr % 50 == 0:
            print(f"Iteration #{itr} loss: {loss_value}")

        itr += 1

    # update the learning rate
    if lr_scheduler is not None:
        lr_scheduler.step()

    print(f"Epoch #{epoch} loss: {loss_hist.value}") 

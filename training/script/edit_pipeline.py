def edit_pipeline(input_num='',input_path=''):
        number = input_num
        number = str(int(int(number) / 2))
        path = input_path[:-6]

        check_point_path = path+'faster_rcnn_inception_v2_coco_2018_01_28/model.ckpt'
        t_input_path = path+'train.record'
        t_label_path = path+'labelmap.pbtxt'
        num_example = number
        e_input_path = path+'test.record'
        e_label_path = path+'labelmap.pbtxt'
        f = open('/frcnn_docker/tensorflow1/models/research/object_detection/training/pipeline.config', 'r')
        text = f.read()
        f.close()


        x = ''
        y = ''
        for i in range(text.index('fine_tune_checkpoint: '), text.index('eval_input_reader: ')-2):
                x += text[i]
    ################## Check fine_tune_checkpoint ##########################################
        if 'fine_tune_checkpoint: ' not in x[x.index('fine_tune_checkpoint: '):x.index('  from_detection_checkpoint: ')-1]:
                print('fine_tune_checkpoint not found')
        else:
                pass
    # ################## Check train_input_reader ##########################################
        if 'train_input_reader: ' not in x:
                print("train_input_reader not found")
        else:
                if "input_path: " not in x[x.index('train_input_reader: '):x.index('eval_config: ')-2]:
                        print("(train_input_reader)input_path not found!")
                else:
                        pass
                if "label_map_path: " not in x[x.index('train_input_reader: '):x.index('eval_config: ')-2]:
                        print("(train_input_reader)label_map_path not found!")
                else:
                        pass
        # ################## Check eval_config ##########################################
        if 'eval_config: ' not  in x:
                print('eval_config not found')
        else:
                if 'num_examples: ' not in x:
                        print('num_examples not found')
                else:
                        pass

        for j in range(text.index('eval_input_reader: '), len(text)):
                y += text[j]

    # ################## Check eval_input_reader ##########################################
        if 'eval_input_reader: ' not in y:
                print('eval_input_reader not found')
        else:
                if 'input_path: ' not in y[y.index('eval_input_reader: ')::]:
                        print('(eval_input_reader)input_path not found')
                else:
                        pass
                if 'label_map_path: ' not in y[y.index('eval_input_reader: ')::]:
                        print('(eval_input_reader)label_map_path not found')
                else:
                        pass
        write_check_point = x.replace(x[x.index('fine_tune_checkpoint: ')+len('fine_tune_checkpoint: ')+1:x.index('  from_detection_checkpoint: ')-2], check_point_path)
        write_t_input_path = write_check_point.replace(x[x.index('input_path: ')+len('input_path: ')+1:x.index('  label_map_path: ')-6], t_input_path)
        write_t_lable_map_path = write_t_input_path.replace(x[x.index('label_map_path: ')+len('label_map_path: ')+1:x.index('eval_config: ')-5], t_label_path)
        write_num_example = write_t_lable_map_path.replace(x[x.index('num_examples: ')+len('num_examples: ')::], num_example)
        write_e_input_path = y.replace(y[y.index('input_path: ')+len('input_path: ')+1:y.index('  label_map_path: ')-6], e_input_path)
        write_e_label_map_input = write_e_input_path.replace(y[y.index('label_map_path: ')+len('label_map_path: ')+1:y.index('  shuffle:')-2], e_label_path)

        result_x = text.replace(text[text.index('fine_tune_checkpoint: '):text.index('eval_input_reader: ')-2], write_num_example)
        result_y = result_x.replace(text[text.index('eval_input_reader: '):len(text)], write_e_label_map_input)

        result = result_y
        print("Edit pipeline.config completed")
        w = open('/frcnn_docker/tensorflow1/models/research/object_detection/training/pipeline.config', 'w+')
        w.write(result)
        w.close()



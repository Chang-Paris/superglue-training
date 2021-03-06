import torch.utils.data
from dataset import Offline_Dataset
import yaml
from sgmnet.match_model import matcher as SGM_Model
from superglue.match_model import matcher as SG_Model
import torch.distributed as dist
import torch
import os
from collections import namedtuple
from train import train
from config import get_config, print_usage


def main(config,model_config):
    """The main function."""
    # Initialize network
    print(config)
    print(model_config)
    if config.model_name=='SGM':
        model = SGM_Model(model_config)
    elif config.model_name=='SG':
        model= SG_Model(model_config)
    else:
        raise NotImplementedError
    print(model)

    #initialize cuda
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Setting device to {device}')
    model.to(device)

    #initialize dataset
    train_dataset = Offline_Dataset(config,'train')
    train_loader=torch.utils.data.DataLoader(train_dataset, batch_size=config.train_batch_size,
           collate_fn=train_dataset.collate_fn, shuffle=True)

    valid_dataset = Offline_Dataset(config,'valid')
    valid_loader=torch.utils.data.DataLoader(valid_dataset, batch_size=config.train_batch_size,
                collate_fn=valid_dataset.collate_fn, shuffle=True)
    
    print('start training .....')
    train(model,train_loader, valid_loader, config,model_config, device)

if __name__ == "__main__":
    # ----------------------------------------
    # Parse configuration
    config, unparsed = get_config()
    print(os.path.exists(config.config_path), config.config_path)
    with open(config.config_path, 'r') as f:
        model_config = yaml.load(f)
    model_config=namedtuple('model_config',model_config.keys())(*model_config.values())
    # If we have unparsed arguments, print usage and exit
    if len(unparsed) > 0:
        print_usage()
        exit(1)

    main(config,model_config)

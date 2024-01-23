from pathlib import Path

def get_conf():
    return {
        'batch_size':8,
        'num_epochs':20,
        'lr':10**-4,
        'seq_len':350,
        'd_model':512,
        'lang_src':'en',
        'lang_tgt':'it',
        'model_folder':'weights',
        'model_filename': 'tmodel_',
        'preload': None,
        'tokenizer_file':'tokenizer_{0}.json',
        'expermient_name': 'runs/tmodel'
    }

def get_weights_file_path(conf,epoch:str):
    model_folder = conf['model_folder']
    model_basename = conf['model_basename']
    model_filename = f'{model_basename}{epoch}.pt'
    return str(Path('.') / model_folder / model_filename)

def latest_weights_file_path(config):
    model_folder = f"{config['datasource']}_{config['model_folder']}"
    model_filename = f"{config['model_basename']}*"
    weights_files = list(Path(model_folder).glob(model_filename))
    if len(weights_files) == 0:
        return None
    weights_files.sort()
    return str(weights_files[-1])
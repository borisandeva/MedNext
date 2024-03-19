from batchgenerators.utilities.file_and_folder_operations import *
import numpy as np

if __name__ == '__main__':
    # input_file = '/home/fabian/data/nnUNet_preprocessed/Task004_Hippocampus/nnUNetPlansv2.1_plans_3D.pkl'
    # output_file = '/home/fabian/data/nnUNet_preprocessed/Task004_Hippocampus/nnUNetPlansv2.1_LISA_plans_3D.pkl'
    
    input_file = '/home/joan/Projects/MedNext/mednext/dataset/nnUNet_preprocessed/Task007_Pancreas/nnUNetPlansv2.1_plans_3D.pkl'
    output_file = '/home/joan/Projects/MedNext/mednext/dataset/nnUNet_preprocessed/Task007_Pancreas/nnUNetPlansv2.1_plans_3D.pkl'
    a = load_pickle(input_file)
    a['plans_per_stage'][0]['batch_size'] = 1
    print('changed batch size to: ', a['plans_per_stage'][0]['batch_size'])
    save_pickle(a, output_file)
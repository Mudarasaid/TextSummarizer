from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: Path
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path

@dataclass
class ModelTrainigCinfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int                 # Number of times to loop over the entire dataset during training
    warmup_steps: int                     # Number of warmup steps for learning rate scheduler
    per_device_train_batch_size: int      # Batch size per device (GPU/CPU) during training 
    weight_decay: float                   # L2 weight decay for regularization 
    logging_steps: int                    # Log training metrics every 10 steps
    evaluation_strategy: str              # Evaluate every N steps 
    eval_steps: int                       # Run evaluation every 500 steps
    save_steps: float                     # Save model every 1,000,000 steps 
    gradient_accumulation_steps: int      # Accumulate gradients over 16 steps before backpropagation
    

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path
    
    
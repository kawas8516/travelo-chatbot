# llm_integration/fine_tune.py
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import Dataset
import json
import os

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Set padding token for consistency
tokenizer.pad_token = tokenizer.eos_token  # Using the EOS token as the PAD token

# Load and prepare dataset
with open('C:/Users/kaust/Envs/travelo/llm_integration/training_data.json', 'r') as f:
    raw_data = json.load(f)

# Structure dataset in Hugging Face format
data_dict = {
    "prompt": [entry["prompt"] for entry in raw_data],
    "response": [entry["response"] for entry in raw_data]
}
dataset = Dataset.from_dict(data_dict)

# Preprocessing function
def preprocess_function(examples):
    inputs = tokenizer(examples["prompt"], truncation=True, padding="max_length", max_length=50)
    labels = tokenizer(examples["response"], truncation=True, padding="max_length", max_length=50)
    inputs["labels"] = labels["input_ids"]
    return inputs

# Apply preprocessing to dataset
tokenized_dataset = dataset.map(preprocess_function, batched=True)

# Training configuration
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="no",  # No evaluation dataset specified
    learning_rate=2e-5,
    per_device_train_batch_size=2,
    num_train_epochs=3,
    weight_decay=0.01,
    save_steps=500,  # Save checkpoint after 500 steps
)

# Initialize Trainer for training
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

# Fine-tune the model
trainer.train()

# Saving model and tokenizer to the specified directory
output_dir = "./trained_model"
model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)
print(f"Model and tokenizer saved in {output_dir}")

model.push_to_hub("kawas8516/travelo")
tokenizer.push_to_hub("kawas8516/travelo")

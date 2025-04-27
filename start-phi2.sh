#!/bin/bash
/home/neofto/Projects/llms/llamafile/o/llama.cpp/main/main \
  -m /home/neofto/Projects/llms/llamafile/phi-2.Q4_K_M.gguf \ #TODO: change to your model path
  --port 8081 \
  --server \
  --nobrowser
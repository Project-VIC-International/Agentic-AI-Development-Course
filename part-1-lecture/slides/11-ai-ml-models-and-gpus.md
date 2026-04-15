# AI/ML Models & GPUs

---

## LLMs Are Not the Only AI

Large Language Models (ChatGPT, Claude) are what you've heard the most about. But the AI ecosystem is much broader.

**AI/ML Models** are specialized programs trained to perform specific tasks:

- **Image classification** — is this image CSAM? What category?
- **Object detection** — what's in this image? Where are the faces?
- **Natural language processing** — extract entities from a report
- **Hash matching** — perceptual hashing to find near-duplicate images
- **Age estimation** — estimate the age of a person in an image
- **Network analysis** — detect patterns in communication graphs

These models are trained, shared, and deployed — and you can get them from multiple sources.

---

## Where to Get Models

### HuggingFace — The Model Library

[HuggingFace](https://huggingface.co) is the GitHub of AI/ML models. Thousands of pre-trained models, free to download and use.

- Search by task: "image classification," "text extraction," "object detection"
- Models come with documentation, benchmarks, and usage examples
- Many have permissive licenses (Apache 2.0, MIT)

### The Research Community

- Academic papers often publish models alongside their research
- Conferences like AAAI, NeurIPS, and CVPR produce models applicable to forensics
- Researchers may collaborate on mission-specific models

### Project VIC International

- Provides models and tools specifically for child exploitation investigations
- Hash intelligence (VICS) is the most widely adopted
- Domain-specific models trained on relevant datasets

### Your State University

- Universities have AI/ML research labs, GPU clusters, and graduate students
- Many have partnerships with law enforcement
- They can train **custom models** on your specific problem domain
- They understand research ethics, data handling, and validation requirements

**You don't have to build models from scratch.** Search for existing ones first, then partner with experts to customize.

---

## Why GPUs Matter: Hardware Acceleration

### What Is a GPU?

A **Graphics Processing Unit** — originally designed for rendering graphics, now essential for running AI models.

### Why Can't a Regular Computer (CPU) Do This?

| CPU (Central Processing Unit) | GPU (Graphics Processing Unit) |
|-------------------------------|-------------------------------|
| A few powerful cores | Thousands of smaller cores |
| Processes tasks one at a time | Processes thousands in parallel |
| Good for general computing | Built for massive parallel math |
| Runs an LLM slowly | Runs an LLM at usable speed |

### The Speed Difference

AI models perform millions of mathematical operations per inference (each time they process an input):

- **CPU only:** Processing one image might take 5-10 seconds
- **GPU accelerated:** Same image in milliseconds
- **For a batch of 10,000 images:** CPU = hours. GPU = minutes.

### What This Means for Your Mission

- **Real-time inference** — classify images as they're extracted, not in a batch overnight
- **Scale** — process the volume of evidence modern cases produce
- **Local processing** — run models on your own hardware, keeping data in your control

### Where GPUs Live

- **In your forensic workstation** — NVIDIA GPUs can be added to desktops
- **In cloud services** — AWS, Azure, Google Cloud offer GPU instances
- **In your agency's data center** — if your IT supports it
- **At your university partner** — academic GPU clusters

---

## Key Takeaway

You don't have to train models yourself. You need to know:

1. **Where to find them** — HuggingFace, research community, Project VIC, universities
2. **Why GPUs matter** — they make models fast enough to be useful in real investigations
3. **How to evaluate them** — which brings us to our next critical topic: testing and validation

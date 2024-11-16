# cache

This folder is the cache directory for Hugging Face (HF).

When using online mode, downloaded models will be cached in this folder.

For [offline mode](https://huggingface.co/docs/transformers/main/installation#offline-mode) use, please download the models in advance and specify the model directory,
such as the `xiaoyao9184/easyocr` model below.

The folder structure for `./cache/huggingface/hub/models--xiaoyao9184--easyocr` is as follows.

```
.
├── blobs
│   ├── 034c56a14fd99e766d3f22782b202e09b3f4f44f36fe35dc7abd574eca253c11
│   ├── 12ac21f6f864fff2802d2df0706bc0330548511b994edd6a9afe76917d058256
│   ├── 19ecc60f4e079eb2cd7f25f3513fc996cf80819fc1f1d0aee24c58402cc4776d
│   ├── 1a8d0abb2032c0ec9d06639bc078b7686c10cf3b8193fe42a6382bc6846ae4a3
│   ├── 1e5e3336a4d4923da6246a76338c02cf9b366cfb3d1a84182bfc3d11df7d5a4d
│   ├── 1f3fcccf32e221cfec1debad0a4fd4712685d41403bf0cc21020a614e9a327b2
│   ├── 28d10d7dab96bf38c1d190d09a65a732130f5f34b28dcbd7e51aba3366146896
│   ├── 2a9afd42c374deb98aed0b53c9b77d75e1d00d4e0501f3b0276c54190c89b1a8
│   ├── 3cc308972bccb2c483741e90e87f2941c1b40d84cf548115f48372d288deb0f0
│   ├── 3ebbb9321b9c7c694e169cd23cc37f3c0bd2a160f5b539602bbef80e663e0a17
│   ├── 48d0f3b58f28aa64651ab1032cc2d498c4de25135829668e87c14e7a07529f29
│   ├── 4a5efbfb48b4081100544e75e1e2b57f8de3d84f213004b14b85fd4b3748db17
│   ├── 56821c103a44e2852b01557514e4f0b6f67e6bce78b2037e17b3891334280d2a
│   ├── 872270d09e64ba9c1bef83a722edae0e9856239f
│   ├── a6344aac8c09253b3b630fb776ae94478aa0275b
│   ├── a73ba1c65f8b3e7b18df3104c1f137970510ce51e3e1d9341506292730fa3c43
│   ├── aaa95be1c4a9cb3496879bed7c520886ce1164f89e026f0c54488394e74e8c55
│   ├── afbb32b0485297de5a7c1f59aeecac12c69f32b15cedd3c3d8c2e8529de85af3
│   ├── cb678fdef09d651e7763ca551ad790dc89f0b2e3d2a640484330e338fb574c7a
│   ├── d4b2252198ef75ee123c727fe406088b443d1403a39fc8fcdcb4c6b04a2583a6
│   ├── d639aa54484314bf4125bb6f59088cfa5162f3d089ebccf3a9d8c6c362776856
│   ├── e2272681d9d67a04e2dff396b6e95077bc19001f8f6d3593c307b9852e1c29e8
│   └── ecdead53c909748aad74bc2f2beeab3e3ad751134db6335e97ea19f879ca407e
├── refs
│   └── master
└── snapshots
    └── 17cdb173ef73b32eb6e9d1270f33b30154b03908
        ├── arabic.pth -> ../../blobs/2a9afd42c374deb98aed0b53c9b77d75e1d00d4e0501f3b0276c54190c89b1a8
        ├── bengali.pth -> ../../blobs/28d10d7dab96bf38c1d190d09a65a732130f5f34b28dcbd7e51aba3366146896
        ├── chinese.pth -> ../../blobs/19ecc60f4e079eb2cd7f25f3513fc996cf80819fc1f1d0aee24c58402cc4776d
        ├── chinese_sim.pth -> ../../blobs/56821c103a44e2852b01557514e4f0b6f67e6bce78b2037e17b3891334280d2a
        ├── craft_mlt_25k.pth -> ../../blobs/4a5efbfb48b4081100544e75e1e2b57f8de3d84f213004b14b85fd4b3748db17
        ├── cyrillic_g2.pth -> ../../blobs/48d0f3b58f28aa64651ab1032cc2d498c4de25135829668e87c14e7a07529f29
        ├── cyrillic.pth -> ../../blobs/1f3fcccf32e221cfec1debad0a4fd4712685d41403bf0cc21020a614e9a327b2
        ├── devanagari.pth -> ../../blobs/1a8d0abb2032c0ec9d06639bc078b7686c10cf3b8193fe42a6382bc6846ae4a3
        ├── english_g2.pth -> ../../blobs/e2272681d9d67a04e2dff396b6e95077bc19001f8f6d3593c307b9852e1c29e8
        ├── .gitattributes -> ../../blobs/a6344aac8c09253b3b630fb776ae94478aa0275b
        ├── japanese_g2.pth -> ../../blobs/afbb32b0485297de5a7c1f59aeecac12c69f32b15cedd3c3d8c2e8529de85af3
        ├── japanese.pth -> ../../blobs/d639aa54484314bf4125bb6f59088cfa5162f3d089ebccf3a9d8c6c362776856
        ├── kannada.pth -> ../../blobs/3cc308972bccb2c483741e90e87f2941c1b40d84cf548115f48372d288deb0f0
        ├── korean_g2.pth -> ../../blobs/ecdead53c909748aad74bc2f2beeab3e3ad751134db6335e97ea19f879ca407e
        ├── korean.pth -> ../../blobs/034c56a14fd99e766d3f22782b202e09b3f4f44f36fe35dc7abd574eca253c11
        ├── latin_g2.pth -> ../../blobs/aaa95be1c4a9cb3496879bed7c520886ce1164f89e026f0c54488394e74e8c55
        ├── latin.pth -> ../../blobs/12ac21f6f864fff2802d2df0706bc0330548511b994edd6a9afe76917d058256
        ├── pretrained_ic15_res18.pt -> ../../blobs/d4b2252198ef75ee123c727fe406088b443d1403a39fc8fcdcb4c6b04a2583a6
        ├── README.md -> ../../blobs/872270d09e64ba9c1bef83a722edae0e9856239f
        ├── tamil.pth -> ../../blobs/1e5e3336a4d4923da6246a76338c02cf9b366cfb3d1a84182bfc3d11df7d5a4d
        ├── telugu.pth -> ../../blobs/a73ba1c65f8b3e7b18df3104c1f137970510ce51e3e1d9341506292730fa3c43
        ├── thai.pth -> ../../blobs/3ebbb9321b9c7c694e169cd23cc37f3c0bd2a160f5b539602bbef80e663e0a17
        └── zh_sim_g2.pth -> ../../blobs/cb678fdef09d651e7763ca551ad790dc89f0b2e3d2a640484330e338fb574c7a

4 directories, 47 files
```

It will use `./cache/huggingface/hub/models--xiaoyao9184--easyocr/snapshots/17cdb173ef73b32eb6e9d1270f33b30154b03908`.

For more details, refer to [up@cpu-offline/docker-compose.yml](./../docker/up@cpu-offline/docker-compose.yml).


## Pre-download for offline mode

Running in online mode will automatically download the model.

install cli

```bash
pip install -U "huggingface_hub[cli]"
```

download model

```bash
huggingface-cli download xiaoyao9184/easyocr --repo-type model --revision master --cache-dir ./cache/huggingface/hub
```
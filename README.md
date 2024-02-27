## BNaT
> Blockchain Network Attack Traffic dataset

## Dataset overview


## How to use

## Data explorer

| duration | protocol_type | service | src_bytes | dst_bytes | flag | count | srv_count | serror_rate | same_srv_rate | diff_srv_rate | srv_serror_rate | srv_diff_host_rate | dst_host_count | dst_host_srv_count | dst_host_same_srv_rate | dst_host_diff_srv_rate | dst_host_same_src_port_rate | dst_host_serror_rate | dst_host_srv_diff_host_rate | dst_host_srv_serror_rate | label  |
| -------- | ------------- | ------- | --------- | --------- | ---- | ----- | --------- | ----------- | ------------- | ------------- | --------------- | ------------------ | -------------- | ------------------ | ---------------------- | ---------------------- | --------------------------- | -------------------- | --------------------------- | ------------------------ | ------ |
| 0        | tcp           | http    | 408       | 0         | OTH  | 14    | 13        | 0           | 0.64          | 0.36          | 0               | 0.31               | 14             | 13                 | 0.64                   | 0.36                   | 0.21                        | 0                    | 0.31                        | 0                        | MitM   |
| 0        | tcp           | other   | 66        | 0         | OTH  | 5     | 15        | 0           | 1             | 0             | 0               | 0.67               | 5              | 15                 | 1                      | 0                      | 0.31                        | 0                    | 0.67                        | 0                        | Normal |
| 0        | tcp           | other   | 66        | 0         | OTH  | 1045  | 2549      | 0           | 1             | 0             | 0               | 0.59               | 50             | 96                 | 1                      | 0                      | 0.52                        | 0                    | 0.48                        | 0                        | Normal |
| 0        | tcp           | http    | 232       | 0         | OTH  | 12    | 32        | 0           | 1             | 0             | 0               | 0.62               | 12             | 32                 | 1                      | 0                      | 0.36                        | 0                    | 0.62                        | 0                        | Normal |
| 0        | tcp           | other   | 66        | 0         | OTH  | 9     | 23        | 0           | 1             | 0             | 0               | 0.61               | 9              | 23                 | 1                      | 0                      | 0.38                        | 0                    | 0.61                        | 0                        | Normal |
| 0        | tcp           | http    | 294       | 0         | OTH  | 0     | 71        | 0           | 0             | 0             | 0               | 1                  | 0              | 71                 | 0                      | 0                      | 0.33                        | 0                    | 1                           | 0                        | BP     |
| 0        | tcp           | http    | 834       | 435       | S1   | 22    | 14        | 0.05        | 0.45          | 0.55          | 0.07            | 0.29               | 22             | 14                 | 0.45                   | 0.55                   | 0                           | 0.05                 | 0.29                        | 0.07                     | MitM   |
| 0        | tcp           | other   | 66        | 0         | OTH  | 563   | 54        | 0           | 0.05          | 0.95          | 0               | 0.52               | 58             | 6                  | 0.03                   | 0.97                   | 0.14                        | 0                    | 0.67                        | 0                        | Normal |
| 0        | tcp           | http    | 169       | 0         | OTH  | 9     | 23        | 0           | 1             | 0             | 0               | 0.61               | 9              | 23                 | 1                      | 0                      | 0.38                        | 0                    | 0.61                        | 0                        | Normal |
| 0        | tcp           | http    | 60        | 0         | S1   | 329   | 343       | 0.88        | 0.98          | 0.02          | 0.84            | 0.06               | 100            | 100                | 1                      | 0                      | 0                           | 1                    | 0                           | 1                        | DoS    |
| 0        | tcp           | other   | 258       | 0         | OTH  | 1     | 5         | 0           | 1             | 0             | 0               | 0.8                | 1              | 5                  | 1                      | 0                      | 0.5                         | 0                    | 0.8                         | 0                        | Normal |
| 0        | tcp           | other   | 66        | 0         | OTH  | 4     | 5         | 0           | 1             | 0             | 0               | 0.2                | 4              | 5                  | 1                      | 0                      | 0                           | 0                    | 0.2                         | 0                        | Normal |
| 0        | tcp           | http    | 599       | 526       | SF   | 1     | 1         | 0           | 1             | 0             | 0               | 0                  | 1              | 1                  | 1                      | 0                      | 0                           | 0                    | 0                           | 0                        | Normal |
| 0        | tcp           | other   | 66        | 0         | OTH  | 597   | 985       | 0           | 0.94          | 0.06          | 0               | 0.43               | 49             | 96                 | 0.96                   | 0.04                   | 0                           | 0                    | 0.51                        | 0                        | Normal |
| 0        | tcp           | http    | 295       | 0         | OTH  | 0     | 3         | 0           | 0             | 0             | 0               | 1                  | 0              | 3                  | 0                      | 0                      | 0                           | 0                    | 1                           | 0                        | BP     |
| 0        | tcp           | other   | 66        | 0         | OTH  | 51    | 68        | 0           | 0.92          | 0.08          | 0               | 0.31               | 51             | 68                 | 0.92                   | 0.08                   | 0                           | 0                    | 0.31                        | 0                        | Normal |
| 0        | tcp           | other   | 66        | 0         | OTH  | 47    | 70        | 0           | 0.91          | 0.09          | 0               | 0.39               | 47             | 70                 | 0.91                   | 0.09                   | 0                           | 0                    | 0.39                        | 0                        | Normal |
| 0        | tcp           | http    | 406       | 0         | OTH  | 17    | 13        | 0           | 0.59          | 0.41          | 0               | 0.23               | 17             | 13                 | 0.59                   | 0.41                   | 0.14                        | 0                    | 0.23                        | 0                        | MitM   |
| 0        | tcp           | http    | 409       | 0         | OTH  | 1729  | 3014      | 0           | 0.97          | 0.03          | 0               | 0.44               | 53             | 95                 | 0.94                   | 0.06                   | 0.09                        | 0                    | 0.47                        | 0                        | FoT    |
| 0        | tcp           | http    | 181       | 0         | OTH  | 2     | 8         | 0           | 1             | 0             | 0               | 0.75               | 2              | 8                  | 1                      | 0                      | 0.22                        | 0                    | 0.75                        | 0                        | Normal |
| 0        | tcp           | http    | 392       | 0         | OTH  | 7     | 3         | 0           | 0.43          | 0.57          | 0               | 0                  | 7              | 3                  | 0.43                   | 0.57                   | 0                           | 0                    | 0                           | 0                        | MitM   |
| 0        | tcp           | other   | 66        | 0         | OTH  | 36    | 49        | 0           | 0.83          | 0.17          | 0               | 0.39               | 36             | 49                 | 0.83                   | 0.17                   | 0                           | 0                    | 0.39                        | 0                        | Normal |

## List of references

<span style="color:red">The details of the BNaT dataset were published in following the paper. For the academic/public use of this dataset, the authors have to cite the following paper:</span>

- Tran Viet Khoa, Do Hai Son, Dinh Thai Hoang, Nguyen Linh Trung, Tran Thi Thuy Quynh, Diep N. Nguyen, Nguyen Viet Ha, and Eryk Dutkiewicz, "Collaborative Learning for Cyberattack Detection in Blockchain Networks," *IEEE Transactions on Systems, Man, and Cybernetics: Systems*, pp. 1-15, Feb. 2024. (accepted) [pre-print](https://arxiv.org/abs/2203.11076)

## Referenced by

BNaT is used by the following papers:

## Acknowledgements

This work was supported by the **ASEAN IVO (ICT Virtual Organization of ASEAN Institutes and NICT)** under Project [Cyber-Attack Detection and Information Security for Industry 4.0](https://www.nict.go.jp/en/asean_ivo/ASEAN_IVO_2018_Projects02.html). 

<p float="left" style="text-align-last: center">
  <a href="https://www.nict.go.jp/en/asean_ivo/ASEAN_IVO_2018_Projects02.html" target="_blank"><img src="./assets/img/IVO.png" class="logo"/></a>
</p>

> Docs website is powered by [docsify](https://docsify.js.org/)

文件说明
image: 按顺序排列的图片
prompt.txt: 按顺序排列的文本prompt
results：保存结果的文件夹


操作流程
1. 按编号顺序将images的图片上传，同时复制prompt.txt中对应编号的prompt。让gpt4v进行generation
2. 将结果复制并保存到results/对应编号的txt文件中。
3. 注意，gpt4v有反批量调用的设计，所以问五到十次就需要点new chat新开一个对话框进行询问。
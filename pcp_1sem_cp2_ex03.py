checkpoint_1_nv = float(input('Digite a nota do primeiro checkpoint: '))
checkpoint_2_nv = float(input('Digite a nota do segundo checkpoint: '))
checkpoint_3_nv = float(input('Digite a nota do terceiro checkpoint: '))


sprint_1 = float(input('Digite a nota do primeiro sprint: '))
sprint_2 = float(input('Digite a nota do segundo sprint: '))
global_soluction = float(input('Digite a nota do global solution: '))


if(checkpoint_1_nv <= checkpoint_2_nv and checkpoint_1_nv <= checkpoint_3_nv):
  checkpoint_1 = checkpoint_2_nv
  checkpoint_2 = checkpoint_3_nv
elif(checkpoint_2_nv <= checkpoint_1_nv and checkpoint_2_nv <= checkpoint_3_nv):
  checkpoint_1 = checkpoint_1_nv
  checkpoint_2 = checkpoint_3_nv
else:
  checkpoint_1 = checkpoint_1_nv
  checkpoint_2 = checkpoint_2_nv


media_1_sem_sem_peso = (
  (((checkpoint_1 + checkpoint_2 + sprint_1 + sprint_2) / 4) * 0.4) + 
  (global_soluction * 0.6)
)
media_1_sem_com_peso = ((((checkpoint_1 + checkpoint_2 + sprint_1 + sprint_2) / 4) * 0.4) + (global_soluction * 0.6)) * 0.4
print(f'A média do semestre sem peso e com peso é respectivamente: {media_1_sem_sem_peso:.2f} e {media_1_sem_com_peso:.2f}.')
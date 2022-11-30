#include<stdio.h>
#include<readline/history.h>

int main(){

  HIST_ENTRY * new_entry = replace_history_entry(1,"ls",date);

  if(new_entry == NULL){
    exit(1);
  }

  printf("hello world");
  return 0;
}


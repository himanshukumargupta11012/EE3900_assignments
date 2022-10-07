#include<stdio.h>
#include<stdlib.h>

struct node{
int data;
struct node* before;
struct node* next;
};


void create(struct node* head,struct node* point,int num){
point->data=num;
point->before=head;
point=point->next;
}


void display(struct node* head){
  if(head->next->next!=NULL){
    printf("%d/n",head->data);
    display(head->next);

  }



}
int main(){

  struct node* head=(struct node*)(calloc(sizeof(struct node*),1)); 
  struct node* point=head->next; 
  head->data=0;
  create(head,point,1);
  return 0;
}




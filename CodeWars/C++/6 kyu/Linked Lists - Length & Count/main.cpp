/* Node Definition
struct Node {
  Node * next;
  int data;
}
*/

int Length(Node *head)
{
  auto lenght = 0;
  while(head) 
  {
    ++lenght;
    head = head->next;
  }
  return lenght;
}

int Count(Node *head, int data)
{
  auto count = 0;
  while(head) 
  {
    if(head->data == data) ++count;
    head = head->next;
  }
  return count;
}
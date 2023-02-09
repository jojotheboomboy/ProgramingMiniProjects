public class Stack<T>
{
	List<T> list;
	
	public Stack() 
	{
		list = new List<T>();
	}
	
	public Stack(Stack<T> j)
	{
		if (j == null) return;
		this.list = new List<T>(j.list);
	}
	
	public void Push(T value)
	{
		list.First();
		list.InsertBefore(value);
		list.First();
	}
	
	public T Pop()
	{
		list.First();
		T temp = list.GetValue();
		list.Remove();
		return temp;
	}
	
	public int Size()
	{
		return list.GetSize();
	}
	
	public T Peek()
	{
		list.First();
		T temp = list.GetValue();
		return temp;
	}
	
	public boolean IsEmpty()
	{
		return list.IsEmpty();
	}
	
	public boolean IsFull()
	{
		return list.IsFull();
	}
	
	public boolean Equals(Stack<T> h)
	{
		return this.list.Equals(h.list);
	}
	
	public Stack<T> Add(Stack<T> j)
	{
		Stack<T> placeholder = new Stack<T>(this);
		if (j == null) 
			return placeholder;
		placeholder.list = placeholder.list.Add(j.list);
//		for(int i = 0; i < temp.Size(); i++)
//		{
//			placeholder.Push(temp.Pop());
//			
//		}
		return placeholder;
	}
	
	public String toString()
	{
		return list.toString();
	}
}
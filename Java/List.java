/* ***************************************************
 * <~~~Josiah Norman
 * <~~~10/21/2021
 * <~~~List.java
 *
 * < my class, List, uses the object of Node, defined in it's own class, to manipulate and construct linked lists 
 * in a correct and efficient manner >
 *************************************************** */

// the Node class
class Node<T>
{
	private T data;
	private Node<T> link;

	// constructor
	public Node()
	{
		this.data = null;
		this.link = null;
	}

	// accessor and mutator for the data component
	public T getData()
	{
		return this.data;
	}

	public void setData(T data)
	{
		this.data = data;
	}

	// accessor and mutator for the link component
	public Node<T> getLink()
	{
		return this.link;
	}

	public void setLink(Node<T> link)
	{
		this.link = link;
	}
}

// the List class
public class List<T>
{
	public static final int MAX_SIZE = 50;

	private Node<T> head;  		// index of the first item on the list
	private Node<T> tail;			// index of the last item on the list
	private Node<T> curr;			// index of the current item in the list
	private int num_items;

	// constructor
	// remember that an empty list has a "size" of 0 and its "position" is at -1
	public List()
	{
		num_items = 0;
	}

	// copy constructor
	// clones the list l and sets the last element as the current
	public List(List<T> l)
	{
		this.num_items = 0;
		if (l == null) return;
		
		int pos = l.GetPos();
		l.SetPos(0);
		
		for (int i = 0; i < l.num_items; i++) 
		{
			InsertAfter(l.GetValue());
			l.Next();
		}
		
		l.SetPos(pos);
	}

	// navigates to the beginning of the list
	public void First()
	{
		curr = head;
	}

	// navigates to the end of the list
	// the end of the list is at the last valid item in the list
	public void Last()
	{
		curr = tail;
	}

	// navigates to the specified element (0-index)
	// this should not be possible for an empty list
	// this should not be possible for invalid positions
	public void SetPos(int pos)
	{
		if (IsEmpty()) return;
		
		if (pos < 0 || pos >= num_items) return;
			
		curr = head;
		for (int i = 0; i < pos ;i++) {
			Next();
		}
		
	}

	// navigates to the previous element
	// this should not be possible for an empty list
	// there should be no wrap-around
	public void Prev()
	{
		if (IsEmpty()) return;
		
		Node<T> preCurr = head;
		while (preCurr != curr && preCurr.getLink() != curr) {
			preCurr = preCurr.getLink();
		}
		curr = preCurr;
	}

	// navigates to the next element
	// this should not be possible for an empty list
	// there should be no wrap-around
	public void Next()
	{
		if (IsEmpty()) return;
		
		if (curr.getLink() == null) return;
			
		curr = curr.getLink();
	}

	// returns the location of the current element (or -1)
	public int GetPos()
	{
		if (IsEmpty()) return -1;
		
		Node<T> temp = head;
		int counter = 0;
		while (temp != curr) {
			temp = temp.getLink();
			counter++;
		}
		return counter;
		
		
	}

	// returns the value of the current element (or -1)
	public T GetValue()
	{
		//condition ? value_if_true : value_if_false
		return curr == null ? null : curr.getData();
	}

	// returns the size of the list
	// size does not imply capacity
	public int GetSize()
	{
		return num_items;
	}

	// inserts an item before the current element
	// the new element becomes the current
	// this should not be possible for a full list
	public void InsertBefore(T data)
	{
		if (IsFull()) return;
		
		if (IsEmpty()) {
			
			head = new Node<T>();
			head.setData(data);
			curr = head;
			tail = head;
			num_items++;
			return;
		}
		
		Node<T> preCurr = head;
		while (preCurr != curr && preCurr.getLink() != curr) 
		{
			preCurr = preCurr.getLink();
		}
		
		Node<T> newNode = new Node<T>();
		newNode.setData(data);
		newNode.setLink(curr);
		if (preCurr == head && preCurr == curr)
		{
			head = newNode;
		}
		else 
			preCurr.setLink(newNode);
		
		curr = newNode;
		num_items++;
	}

	// inserts an item after the current element
	// the new element becomes the current
	// this should not be possible for a full list
	public void InsertAfter(T data)
	{
		if (IsFull()) return;
		
		if (IsEmpty()) {
			
			head = new Node<T>();
			head.setData(data);
			curr = head;
			tail = head;
			num_items++;
			return;
		}
		
		Node<T> temp = new Node<T>();
		temp.setData(data);
		temp.setLink(curr.getLink());
		curr.setLink(temp);
		
		if (tail == curr)
			tail = temp;

		curr = temp;
		num_items++;
	}

	// removes the current element (collapsing the list)
	// this should not be possible for an empty list. If possible,
	// following element becomes new current element.
	public void Remove()
	{
		if (IsEmpty()) return;
		
		if (curr == head) {
			head = curr.getLink();
			Next();
		} else if (curr == tail) {
			Prev();
			tail = curr;
			curr.setLink(null);
		} else { 
			Node<T> temp = curr;
			Prev();
			curr.setLink(temp.getLink());
			Next();
		}
		
		num_items--;
		
	}

	// replaces the value of the current element with the specified value
	// this should not be possible for an empty list
	public void Replace(T data)
	{
		if (IsEmpty()) return;
		
		curr.setData(data);
	}

	// returns if the list is empty
	public boolean IsEmpty()
	{
		return num_items == 0;
	}

	// returns if the list is full
	public boolean IsFull()
	{
		return num_items == MAX_SIZE;
	}

	// returns if two lists are equal (by value)
	public boolean Equals(List<T> l)
	{
		Node<T> currA = head;
		Node<T> currB = l.head;
		if (GetSize() != l.GetSize()) return false;
		
		for (int i = 0; i < num_items; i++)
		{
			if (currA.getData() != currB.getData())
				return false;
			currA = currA.getLink();
			currB = currB.getLink();
				
		}
		return true;
	}

	// returns the concatenation of two lists
	// l should not be modified
	// l should be concatenated to the end of *this
	// the returned list should not exceed MAX_SIZE elements
	// the last element of the new list is the current
	public List<T> Add(List<T> l)
	{
		List<T> combined = new List<T>(this);
		
		if (l == null) return combined;
		int pos = l.GetPos();
		l.SetPos(0);
		
		for (int i = 0; i < l.GetSize(); i++)
		{
			combined.InsertAfter(l.GetValue());
			l.Next();
		}
		
		l.SetPos(pos);
		return combined;
	}

	// returns a string representation of the entire list (e.g., 1 2 3 4 5)
	// the string "NULL" should be returned for an empty list
	public String toString()
	{
		
		String result = "";
		Node<T> temp = head;
		
		if (IsEmpty()) 
			return "NULL";
		else
			for (int i = 0; i < num_items; i++) 
			{
				result += temp.getData() + " ";
				temp = temp.getLink();
				
			}
		return result;
	}
}
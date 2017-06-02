import React, { Component } from 'react';

class ItemList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      items: [
        {
          _id: '3202-5',
          description: 'bla bla',
        }
      ],
    };
  }

  listItems() {
    return this.state.items.map((item) =>
        <p key={item._id}>{item._id}: {item.description}</p>
    );
  }

  render() {
    return (
      <div className="Item-list">
        <h3>All items</h3>
        { this.listItems() }
      </div>
    );
  }
}

export default ItemList;

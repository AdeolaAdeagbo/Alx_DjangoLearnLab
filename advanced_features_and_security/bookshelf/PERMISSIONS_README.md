# Permissions Setup

## Groups Created
- Viewers: can_view
- Editors: can_view, can_create, can_edit  
- Admins: All permissions

## Views Protected
- book_list: @permission_required('bookshelf.can_view')
- create_book: @permission_required('bookshelf.can_create')
- edit_book: @permission_required('bookshelf.can_edit')
- delete_book: @permission_required('bookshelf.can_delete')
import model
import view



def start():
    pb = model.PhoneBook()
    pb.path
    choice = ''
    while choice != '8':
        choice = view.main_menu()
        match choice:
            case '1':
                pb.open()
                view.information('\nФайл успешно открыт\n')
            case '2':
                pb.save()
                view.information('\nФайл успешно сохранен\n')
            case '3':
                view.show_contacts(pb.get())
            case '4':
                new_contact = list(view.create_new_contact())
                pb.new(new_contact)
                view.information(f'\nКонтакт {new_contact[0][0]} успешно создан\n')
            case '5':
                del_name = view.select_contact('Введите удаляемый контакт: ')
                contact = pb.get_contact(del_name)
                if contact:
                    confirm = view.delete_confirm(contact[0][0])
                    if confirm:
                        pb.delete(contact[0])
                        view.information(f'\nКонтакт {new_contact[0][0]} успешно удален\n')
                elif contact == []:
                    view.empty_request()
                else:
                    view.many_request()
            case '6':
                name = view.select_contact('Введите изменяемый контакт: ')
                contact = pb.get_contact(name)
                if contact:
                    changed_contact = view.change_contact()
                    pb.change_contact(contact[1], list(changed_contact))
                    view.information(f'\nКонтакт {new_contact[0][0]} успешно изменен\n')
                elif contact == []:
                    view.empty_request()
                else:
                    view.many_request()
            case '7':
                find = view.find_contact()
                result = pb.search(find)
                view.show_contacts(result)
            case '8':
                view.end_program()
                break
            case _:
                view.input_error()
# Print the welcome message to  welcome users
print('Welcome to the simple calculator, please select from the following options:')
# Define the selection options
selection_options=('1:Addition','2:Subtraction','3:multiplication','4:divison')
#  Iterate through the selection options and print each one using a for loop
for selection in selection_options:
  print(selection)

# Define a function to check the user's selection
def check_selection():
  #  while loop ensures  the calculator program keeps running until the user decides to exit 
  while(True):
      # Code that might raise an exception is passed in the try block if it passes this block the except block is skipped
      #  if not errors are handeled inside the except block
      try:
       # ask the user to enter their selection
        num_from_selection= input('please enter your selection:')
        # convert a string to integer
        num_from_selection=int(num_from_selection)
        if(num_from_selection in range(1,5)):
          # Code that might raise an exception is passed in the try block, if it passes this block the except block is skipped
          #  if not errors are handeled inside the except block
          try:
              num_one= input('please enter your first number:')
              # Ask the user to enter the first number and second numbers and chnage the string to integer
              num_one= int(num_one)
              num_two= input('please enter your second number:')
              num_two= int(num_two)
              # Return the two numbers
              return num_from_selection,num_one,num_two
          except NameError:
            # Exception handler for a specific exception (NameError)
            print("please choose numbers.")
            # Exception handler for a specific exception (ValueError)
          except ValueError:
            print("please enter numbers only.")
            # Exception handler for a specific exception (TypeError)
          except TypeError:
            print("please selelct appropriate Number value")
            # Generic exception handler (catches all other exceptions)
          except:
            print("Something went wrong, sorry.") 
        else:
            print('please select from number options provided ')
           # Exception handler for a specific exception (NameError)
      except NameError:
            print("please choose numbers only from the selection  options.")
      # Exception handler for a specific exception (ValueError)
      except ValueError:
            print("please enter numbers only, NO Letters or Simbols!.")
      except TypeError:
       print("please selelct appropriate Number value")
       # Generic exception handler (catches all other exceptions)
      except:
        print("Something went wrong, sorry.") 

# Define a function to add two numbers and return the result
def add_two_numbers(num_one,num_two):
  add_result=num_one+num_two
  return add_result

# Define a function to subtract two numbers return the result
def sub_two_numbers(num_one,num_two):
  subtract_values=num_one-num_two
  return subtract_values

# Define a function to multiply two numbers return the result
def multi_two_numbers(num_one,num_two):
  mult_values=num_one*num_two
  return mult_values

# Define a function to divide two numbers return the result
def div_two_numbers(num_one,num_two):
     # Code that might raise an exception
    try:
      divison_values=num_one/num_two
      return divison_values
      # Exception handler for another specific exception (ZeroDivisionError)
    except ZeroDivisionError:
      print("can't divid by 0 please try again")  
       # Generic exception handler (catches all other exceptions)
    except:
      print("Something went wrong, sorry.") 

# Define a function to handle the user's choice for the next calculation
def next_number_calculation(): 
    # Ask the user to enter their choice to use the calculator again (y/n)
    next_entry=input('do you want to use the calculator again?,(y/n)') 
    # Check the user's input and perform the corresponding actions
    if(next_entry=='y'):
    # If the user chooses 'y', clear the selection list and call check_result again
        new_values=check_selection() 
        main_calculator(new_values)
    elif(next_entry=='n'):
    # If the user chooses 'n', clear the selection list and print a goodbye message
        print('Good bye!')
        return
    else:
    # If the user enters neither 'y' nor 'n', ask them to enter a valid input
        print('please inter either y or n & try again')

def main_calculator(check_result):
    while(True):
     # Unpack the values from the check_result tuple and assign them to the variables sel, num_one, and num_two
     # sel represents the selected mathematical operation, while num_one and num_two represent the two numbers chosen by the user
      sel,num_one,num_two=check_result
    # Perform addition if selection is 1
      if(sel==1):
          add_result=add_two_numbers(num_one,num_two)
          print(add_result)
    # Perform subtraction if selection is 2
      elif(sel==2):
          sub_result=sub_two_numbers(num_one,num_two)
          print(sub_result)
    # Perform multiplication if selection is 3
      elif(sel==3):
          multi_result=multi_two_numbers(num_one,num_two)
          # round result to the nearest whole number
          print(round(multi_result*0.1))
     # Perform division if selection is 4
      elif(sel==4):
          div_result=div_two_numbers(num_one,num_two)
          print(div_result)
    # Call the next_number_calculation function to ask if the user wants to perform another calculation
      next_number_calculation()
      # Exit the while loop using break
      break

# Call the check_selection function to check the user's selection
check_result=check_selection()
# Call the main_calculator function with the initial check_result
main_calculator(check_result)   




      
      

            
# Print the welcome message to  welcome users
print('Welcome to the simple calculator, please select from the following options:')
# Define the selection options
selection_options=('1:Addition','2:Subtraction','3:multiplication','4:divison')
#  Iterate through the selection options and print each one using a for loop
for selection in selection_options:
  print(selection)
  
# Initialize an empty selection list
selection_list=[]

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
       # Append the selection to the selection_list
      selection_list.append(num_from_selection)
       # Check if the selection is within the valid range
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
            return num_one,num_two
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
        selection_list.clear()
        check_result
      elif(next_entry=='n'):
      # If the user chooses 'n', clear the selection list and print a goodbye message
        selection_list.clear()
        print('Good bye!')
      else:
      # If the user enters neither 'y' nor 'n', ask them to enter a valid input
        print('please inter either y or n')

while(True):
  # Call the check_selection function to check the user's selection
  check_result=check_selection()
# Iterate through the selection list
  for sel in selection_list :
 # Perform addition if selection is 1
      if(sel==1):
          # Assign the checked result (num_one, num_two) to variables
          num_one,num_two=check_result
          # Call the add_two_numbers function to perform addition
          add_result=add_two_numbers(num_one,num_two)
           # Print the result of the addition
          print(add_result)
          # call the next_number_calculation function to ask if user wants to perform another calculation
          next_number_calculation()
           # Perform subtraction if selection is 2
      elif(sel==2):
            # Assign the checked result (num_one, num_two) to variables
          num_one,num_two=check_result
            # Call the sub_two_numbers function to perform subtraction
          sub_result=sub_two_numbers(num_one,num_two)
           # Print the result of the subtraction
          print(sub_result)
          # call the next_number_calculation function to ask if user wants to perform another calculation
          next_number_calculation()
          # Perform multiplication if selection is 3
      elif(sel==3):
          # Assign the checked result (num_one, num_two) to variables
          num_one,num_two=check_result
          multi_result=multi_two_numbers(num_one,num_two)
          # Call the multi_two_numbers function to perform multiplication
          print(multi_result)
          # Print the result of the multiplication
          next_number_calculation()
          # call the next_number_calculation function to ask if user wants to perform another calculation
      elif(sel==4):
          num_one,num_two=check_result
          # Assign the checked result (num_one, num_two) to variables
          div_result=div_two_numbers(num_one,num_two)
          # Call the div_two_numbers function to perform division
          print(div_result)
          # Print the result of the division
          next_number_calculation()
          # Call the next_number_calculation function to ask if user wants to perform another calculation


      break
 # Exit the while loop using break
         
      



      
      

            
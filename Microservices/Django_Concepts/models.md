null=True,"Controls database storage. If True, the column in the database schema can store a NULL value (meaning ""no value"" or ""missing data"").",Database Level,"Used for fields that are optional in the data layer (e.g., date fields)."

blank=True,"Controls form validation. If True, the field is not required to be filled out on forms (like the Django Admin or a custom form). An empty string ('') will be saved.",Python/Form Level,Used for fields that are optional for the user to submit.

"""
/*
# Save operation can be performed in three ways: 
  1. Using **Manager(objects)** create method. 
     * Models.objects.create(eno = '123', ename = 'emp-101')

  2. Using **Save** method.
     * emp = Employee(eno = '123', ename = 'emp-101') --> Creating a model instance
       emp.save()

  3. Using ModelForms when we do forms.save() after forms.is_valid()   

    Note: The difference between two is **Create** on it's own first create a model instance and then save it to db. Where as **save()** gives us option to malidate or mutate fields before saving.

    Difference based on model validation: 
     When we perform object using 1st way, we need to explicitely call the full_clean() method inside the overriden save method(). Because create does not explicitely performs model validation and bypass all the validation rules if any.

     But when we go via form and do form.is_valid() it performs model validation for all the fields which was included in the model forms. here we do not need to explicitely call the full_clean() method, You should only need to call a model’s full_clean() method if you plan to handle validation errors yourself, or if you have excluded fields from the ModelForm that require validation.

     Heirarchy when we go via form.is_valid()
     form.is_valid()
      └──> form.full_clean()
             └──> model.full_clean() calls below in the same order as mentioned.
                  ├── clean_fields()
                  ├── clean()
                  └── validate_unique()
                  └── validate_constraints() all the Meta.Constraints or custom constraints (Discussed further)


               For more info: refer to django model validation docs: https://docs.djangoproject.com/en/6.0/ref/models/instances/#validating-objects


*/

/**

# 1️⃣ What actually happens when you define unique=True. ## username = models.CharField(max_length=50, unique=True).

Ans: At Database-level Django creates **__{ UNIQUE INDEX on username }__** and this is not optional. 
     At django level Django knows **“Before saving, I should check that this value doesn’t already exist.”** But the question is, how does it do that: 

     What ModelForm validation ACTUALLY runs? 
     So when we call form.is_valid() this triggers a query like **__{ SELECT 1 FROM user_profile WHERE username = 'saurabh' LIMIT 1; }__** and this operation takes O(logn) time. so form validation is fast even at django level.

     ** Race condition scenario: **
      User A validates username "alex"
      User B validates username "alex"
      Both pass form validation
      Both try to save
      One fails at DB level

      👉 DB is the FINAL authority

**/

"""

"""
# Which model will have the Foreign Key(FK) field?
 *** ANS: The model or table which is at the many side will hold the Foreign-key field. For ex of Book and author, where an author can have multiple books, keeping FK field on book side would be beneficial because if we keep FK on author at the end we will have duplicate rows only the book column will be unique.
 
 ## INCORRECT Design where Author table is having FK i.e. book_id. See the duplication of records(name)
   Author Table (WRONG)
   | id | name         | book_id |
   | -- | ------------ | ------- |
   | 1  | J.K. Rowling | 101     |
   | 2  | J.K. Rowling | 102     |
   | 3  | J.K. Rowling | 103     |

   BOOK Table
   | id  | title                 |
   | --- | --------------------- |
   | 101 | Harry Potter - Part 1 |
   | 102 | Harry Potter - Part 2 |
   | 103 | Harry Potter - Part 3 |

   ## Correct Design (No Duplication of entries)
   AUTHOR Table 
   | id | name         |
   | -- | ------------ |
   | 1  | J.K. Rowling |

   BOOK Table
   | id  | title                 | author_id |
   | --- | --------------------- | --------- |
   | 101 | Harry Potter - Part 1 | 1         |
   | 102 | Harry Potter - Part 2 | 1         |
   | 103 | Harry Potter - Part 3 | 1         |



# Which model should hold the OneToOne field? 
*** ANS: The model or table which can not exist solely or independently will hold the OneToOne field. FOr ex in case of User and UserProfile, UserProfile will hold the OneToOne field as UserProfile has no existance if User is not present.

"""

"""
# Model level validation : We use/override clean method to perform model level validation. For ex, if we need to validate joining date should not be earlier than company foundation date :

class Employee(models.Model):
    joining_date = models.DateField()

    def clean(self):
        if self.joining_date < date(2010, 1, 1):
            raise ValidationError("Employee cannot join before 2010")

But django does not automatically calls the clean method when you save it. FOr that you will have to override the save method to call the clean before save.

  def save(self, *args, **kwargs):
    self.full_clean()   # calls clean_fields(), clean(), validate_unique()
    super().save(*args, **kwargs)     

 *** NOTE: 1. clean can also be implemented at per fields level such as clean_name or clean_age etc.  
           2. clean also exist at forms level validation. we can implement clean for fields while input parsing at form level 

# What is constraints in django model and how do we implement it? 
  ANS:  Django provides several ways to enforce data integrity and business rules through constraints, primarily via model fields, the Meta.constraints option, and model/form validation methods. 

   1. Field-level Constraints :
   Many standard database constraints are built directly into Django model fields as attributes: 

   ** primary_key=True: Uniquely identifies each row in the table.
   ** unique=True: Ensures all values in a specific column are distinct.
   ** null=False (the default for most fields): Ensures a column cannot store NULL values (a "NOT NULL" constraint).
   ** choices: Restricts a field's value to a specific set of options.
   ** default: Provides a default value if one is not specified during object creation.
   ** max_length: Enforces length limits for CharField and similar fields.
   ** EmailField: Includes built-in validation for valid email addresses. 


   2. For more complex, database-level constraints involving multiple fields or custom conditions, you use the constraints list within your model's Meta options: 

   from django.db import models
   from django.db.models import CheckConstraint, Q, F

   class Event(models.Model):
      start_date = models.DateTimeField()
      end_date = models.DateTimeField()

      class Meta:
         constraints = [
               # Ensures end_date is always greater than start_date at the DB level
               CheckConstraint(
                  check=Q(end_date__gt=F('start_date')),
                  name='check_start_date_before_end_date',
               ),
               # Ensures a combination of fields is unique
               models.UniqueConstraint(
                  fields=['field_one', 'field_two'],
                  name='unique_together_constraint_name'
               ),
         ]
 *** NOTE: Constraints are checked during the model validation phase or simply when we insert or update in db.         

# What is the difference between constraints and validation ?
 ANS:  Validation checks whether data is acceptable
       Constraints enforce what is allowed to exist

       ex: 1️⃣ Validation — Soft rules (logic-level)
            Examples:
              Age must be ≥ 18
              Joining date cannot be before company start date
              Password must contain a special character

            2️⃣ Constraints — Hard rules (database-level) :
            Examples:
               Email must be unique
               Foreign key must exist
               Code must be uppercase
               Quantity must be ≥ 0 

 ** NOTE: If we want to perform validation for any fields at model level only and only clean() must be implemented as django/Models.full_clean() will call it. we can not have clean_fields() as we did in case of forms at model level as django does not call it.


"""
"""
DB Models
Postgres
Saved Companies Table
"""

from extensions_sql import db


class SavedCompany(db.Model):
    """
    Many-To-Many relationship that stores the ID of a company and
    user-defined data such as list name and order.
    """
    __bind_key__ = "postgres"

    __tablename__ = "saved_company"

    company_id = db.Column(
        db.BigInteger,
        db.ForeignKey('companies.id'),
        primary_key=True
    )

    company = db.relationship(
        'Company',
        back_populates="saved_companies",
        lazy='select',
        viewonly=True
    )

    user_profile_id = db.Column(
        db.BigInteger,
        db.ForeignKey('profiles.id'),
        primary_key=True
    )

    user_profile = db.relationship(
        'Profile',
        back_populates="saved_companies",
        lazy='select',
        viewonly=True
    )

    list_name = db.Column(
        db.VARCHAR(length=32),
        nullable=True,
    )

    order = db.Column(
        db.Integer,
        nullable=True,
    )

    notes = db.Column(
        db.TEXT(),
        nullable=True,
    )

    def __repr__(self):
        """Show info about Listed Job Experience Levels."""

        return ("<SavedCompany "
                
                f"company={str(self.company_id)} "
                
                f"user_profile={str(self.user_profile_id)} "
                
                f"list_name={str(self.list_name)} "
                
                f"order={str(self.order)} "
                
                f"notes={str(self.notes)[:128]} "
                
                ">")

    @db.orm.declared_attr
    def __table_args__(self):
        return (
            db.Index(
                'idx_saved_company_company_id',
                self.company_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_saved_company_profile_id',
                self.user_profile_id,
                postgresql_using='hash'
            ),
        )

    def to_dict_rest(self):
        return {
            self.company_id,
            self.user_profile_id,
            self.list_name,
            self.order,
            self.notes,
        }

    def to_dict_rest_complete(self):
        return {
            'list_name': self.list_name,
            'order': self.order,
            'notes': self.notes,

            'id': self.company.id,
            'name': self.company.name,

            'description': (
                self.company.description[:128] + "..."
                if len(self.company.description) > 128
                else self.company.description)
            if self.company.description is not None else 'No Description',

            'websites': self.company.websites
            if self.company.websites is not None else 'None',

            'last_updated': self.company.last_updated,

            'job_count': self.company.current_job_count,
        }

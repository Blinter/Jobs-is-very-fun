"""
DB Models
Postgres
Saved Jobs Table
"""

from extensions_sql import db


class SavedJob(db.Model):
    """
    Many-To-Many relationship that stores the ID of a listed job and
    user-defined data such as list name and order.
    """
    __bind_key__ = "postgres"

    __tablename__ = "saved_job"

    listed_job_id = db.Column(
        db.BigInteger,
        db.ForeignKey('listed_jobs.id'),
        primary_key=True,
        nullable=False,
    )

    listed_job = db.relationship(
        'ListedJob',
        back_populates="saved_jobs",
        lazy='select',
        viewonly=True
    )

    user_profile_id = db.Column(
        db.BigInteger,
        db.ForeignKey('profiles.id'),
        primary_key=True,
        nullable=False,
    )

    user_profile = db.relationship(
        'Profile',
        back_populates="saved_jobs",
        lazy='select',
        viewonly=True,
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

        return ("<SavedJob "
                
                f"listed_job={str(self.listed_job_id)} "
                
                f"user_profile={str(self.user_profile_id)} "
                
                f"list_name={str(self.list_name)} "
                
                f"order={str(self.order)} "
                
                f"notes={str(self.notes)[:128]} "
                
                ">")

    @db.orm.declared_attr
    def __table_args__(self):
        return (
            db.Index(
                'idx_saved_job_listed_job_id',
                self.listed_job_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_saved_job_profile_id',
                self.user_profile_id,
                postgresql_using='hash'
            ),
        )

    def to_dict_rest(self):
        return {
            self.listed_job_id,
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
            'id': self.listed_job.id,
            'name': self.listed_job.name,

            'company': self.listed_job.company.name
            if self.listed_job.company_id is not None else None,

            'salary_currency': self.listed_job.salary_currency
            if (self.listed_job.salary_currency is not None and
                (isinstance(self.listed_job.min_salary, int) and
                 self.listed_job.min_salary > 0) or
                (isinstance(self.listed_job.max_salary, int) and
                 self.listed_job.max_salary > 0))
            else None,

            'min_salary': self.listed_job.min_salary
            if (self.listed_job.salary_currency is not None and
                self.listed_job.min_salary is not None and
                isinstance(self.listed_job.salary_currency, str) and
                isinstance(self.listed_job.min_salary, int) and
                self.listed_job.min_salary > 0)
            else None,

            'max_salary': self.listed_job.max_salary
            if (self.listed_job.salary_currency is not None and
                self.listed_job.max_salary is not None and
                self.listed_job.min_salary is not None and
                isinstance(self.listed_job.salary_currency, str) and
                isinstance(self.listed_job.max_salary, int) and
                isinstance(self.listed_job.min_salary, int) and
                self.listed_job.min_salary > 0)
            else None,

            'location': (
                self.listed_job.listed_job_location[0]
                .listed_job_location.to_jobs_rest())
            if (self.listed_job.listed_job_location is not None and
                len(self.listed_job.listed_job_location) >= 1)
            else None,

            'job_type': (
                self.listed_job.listed_job_experience_levels[0]
                .experience_level.name)
            if (self.listed_job.listed_job_experience_levels is not None and
                len(self.listed_job.listed_job_experience_levels) >= 1)
            else '',

            # 'No Experience Level defined',
            'description': (
                self.listed_job.description[:100] + "..."
                if len(self.listed_job.description) > 100
                else self.listed_job.description)
            if (self.listed_job.description is not None and
                self.listed_job.description != '')
            else 'No Description',

            'posted_time_utc': self.listed_job.posted_time_utc,

            'api_source': self.listed_job.api_source.name[
             self.listed_job.api_source.name.find("|") + 1:].strip(),
        }

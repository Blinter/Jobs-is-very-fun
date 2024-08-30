"""
DB Models
Postgres
Company Table
"""
from sqlalchemy import text

from extensions_sql import db
from sqlalchemy.dialects.postgresql import TSVECTOR
from sqlalchemy.orm.attributes import flag_modified


class Company(db.Model):
    """
    Table that holds information about a company.
    """
    __bind_key__ = "postgres"

    __tablename__ = "companies"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.VARCHAR(),
        nullable=False,
        unique=False
    )

    description = db.Column(
        db.TEXT(),
        nullable=True
    )

    websites = db.Column(
        db.Text(),
        nullable=True,
        unique=False
    )

    last_updated = db.Column(
        db.DateTime(timezone=False),
        nullable=False,
        server_default=text('CURRENT_TIMESTAMP')
    )

    search_vector = db.Column(
        TSVECTOR
    )

    listed_jobs = db.relationship(
        'ListedJob',
        back_populates="company",
        cascade="all, delete",
        lazy='select'
    )

    saved_companies = db.relationship(
        'SavedCompany',
        back_populates="company",
        cascade="all, delete",
        lazy='select'
    )

    listed_job_count = db.Column(
        db.Integer,
        nullable=False,
        default=0,
    )

    expired_listed_job_count = db.Column(
        db.Integer,
        nullable=False,
        default=0,
    )

    current_job_count = db.Column(
        db.Integer,
        nullable=False,
        default=0,
    )

    def __repr__(self):
        """Show info about Company"""

        return ("<Company "
                f"id={str(self.id)} "
                f"name={str(self.name)} " +
                (f"description={str(self.description)[:128]} "
                 if self.description else '') +

                (f"websites={str(self.websites)} "
                 if self.websites else '') +

                f"last_updated={str(self.last_updated)} " +

                ((('[trunc.] ' if len(str(self.listed_jobs)) > 32 else '') +
                  f"listed_jobs={str(self.listed_jobs)[:32]} "
                  if len(str(self.listed_jobs)) > 0 else '')
                 if (self.listed_jobs and
                     self.listed_jobs is not None)
                 else '') +

                ">")

    def to_dict_rest(self):
        """

        """
        return {
            'id': self.id,
            'name': self.name,

            'description': (
                self.description[:128] + "..."
                if len(self.description) > 128 else self.description)
            if self.description is not None else 'No Description',

            'websites': self.websites
            if self.websites is not None else 'None',

            'last_updated': self.last_updated,

            'job_count': self.current_job_count,
        }

    @db.orm.declared_attr
    def __table_args__(self):
        return (
            db.Index(
                'idx_company_vector',
                self.search_vector,
                postgresql_using='gin'
            ),
            db.Index(
                'idx_company_trgm',
                self.name,
                postgresql_using='gin',
                postgresql_ops={
                    'name': 'gin_trgm_ops'
                }
            ),
        )


@db.event.listens_for(Company, 'before_insert')
@db.event.listens_for(Company, 'before_update')
def update_company_search_vector(_, __, target):
    if db.inspect(target).attrs.name.history.has_changes():
        target.search_vector = db.func.to_tsvector(target.name)
        flag_modified(target, "search_vector")

"""
DB Models
Postgres
Listed Job Type Table
"""

from extensions_sql import db


class ListedJobJobType(db.Model):
    """
    Many-To-Many relationship that shows the described Job Type of
    Listed Job.
    """
    __bind_key__ = "postgres"

    __tablename__ = "listed_job_job_types"

    listed_job_id = db.Column(
        db.BigInteger,
        db.ForeignKey('listed_jobs.id'),
        primary_key=True
    )

    listed_job = db.relationship(
        'ListedJob',
        back_populates='listed_job_job_types',
        lazy='select',
        viewonly=True
    )

    job_type_id = db.Column(
        db.Integer,
        db.ForeignKey('job_types.id'),
        primary_key=True
    )

    job_type = db.relationship(
        'JobType',
        back_populates='listed_job_job_types',
        lazy='select',
        viewonly=True
    )

    def __repr__(self):
        """Show info about Listed Job Type."""

        return ("<ListedJobType "
                
                f"listed_job={str(self.listed_job)} " +

                ((('[trunc.]' if len(str(self.job_type)) > 16 else '') +
                  f"job_type={str(self.job_type)[:16]} "
                  if len(str(self.job_type)) > 0 else '')
                 if self.job_type is not None else '') +

                ">")

    @db.orm.declared_attr
    def __table_args__(self):
        return (
            db.Index(
                'idx_listed_job_job_type_listed_job_id',
                self.listed_job_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_listed_job_job_type_job_type_id',
                self.job_type_id,
                postgresql_using='hash'
            ),
        )
